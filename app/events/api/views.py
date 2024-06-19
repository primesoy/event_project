from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from events.models import Category, Event
from .serializers import CategorySerializer
from core.services import call_external_api, ServiceException
from core.mixins import CacheMixin


EXTERNAL_API_URL = "https://friendlybytes.net/api/blog/category/"





class ExternalAPIView(APIView):
    """
    api/events/external?text=asfjkasdjfölk
    """
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




class CategoryListCreateView(CacheMixin, ListCreateAPIView):
    """View zum Auflisten und Anlegen einer Category."""
    serializer_class = CategorySerializer
    queryset = Category.objects.prefetch_related("events", "events__author")
    permission_classes = []