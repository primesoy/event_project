from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
from events.models import Category, Event, MachineType
from .serializers import CategorySerializer, EventSerializer, MachineTypeSerializer
from core.services import call_external_api, ServiceException
from core.mixins import CacheMixin
from drf_spectacular.utils import  extend_schema_view, extend_schema, OpenApiParameter


EXTERNAL_API_URL = "https://friendlybytes.net/api/blog/category/"


class MachineTypeListView(ListAPIView):
    serializer_class = MachineTypeSerializer
    queryset = MachineType.objects.all()


class EventRetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    permission_classes = []



class EventListCreateView(ListCreateAPIView):
    """
    api/events/

    group_size = models.IntegerField(choices=GroupSize.choices)
    curl -X POST http://127.0.0.1:8000/api/events/  -H "Authorization: Token 044f242ea137e2d0dc3a2a51d786cc8921cf179f" -d "name=neuevent&date=2024-12-12T19:50:08&group_size=10&category=3"
    """
    permission_classes = []
    serializer_class = EventSerializer
    queryset = Event.objects.prefetch_related("tags").all()

    def perform_create(self, serializer):
        author = self.request.user  # aktuell eingeloggte user
        serializer.save(author=author)


class CategoryListCreateView(CacheMixin, ListCreateAPIView):
    """View zum Auflisten und Anlegen einer Category."""
    serializer_class = CategorySerializer
    queryset = Category.objects.prefetch_related("events", "events__author")
    permission_classes = []


class ExternalAPIView(APIView):
    """
    api/events/external?text=asfjkasdjfölk
    """
    permission_classes = []

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="text",
                description=(
                    "Searches for the value in this query parameter returning "
                    "all the users that have this value as substring. Ignores lowercase and uppercase."
                ),
                type=str,
            )
        ]
    )
    def get(self, request):

        try:
            text = request.query_params["text"]
            data = call_external_api(
                url=EXTERNAL_API_URL,
                text=text
            )
        
        except KeyError:
            data = {"error": "Parameter text muss angegeben werden"}
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        
        except ServiceException as e:
            data = {"error": str(e)}
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        return Response(data=data, status=status.HTTP_200_OK)





