import logging
import uuid
from rest_framework import generics, permissions, authentication
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

logger = logging.Logger("django")

class EmailConfirmationUserView(View):
    def get(self, request, uid, token):
        try:
            user = get_user_model().objects.get(pk=uid)
        except Exception:
            user = None
            return HttpResponse("User exsitiert nicht")

        # Wenn User schon confirmed ist
        if user and user.email_confirmed:
            return HttpResponse("User ist schon bestätigt.")

        if user and user.email_token == uuid.UUID(token):
            user.email_confirmed = True
            user.save()
            return HttpResponse("Email wurde erfolgreich bestätigt")

        return HttpResponse("Email wurde leider nicht bestätigt")
    

class ListUserView(generics.ListAPIView):
    """Eine View Zum Auflisten von Usern.
    
    api/users/
    """
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


class UserCreateView(generics.CreateAPIView):
    """Einen neuen User anlegen.
    
    api/users/create
    """
    serializer_class = UserSerializer
    permission_classes = []

class ManageUserView(generics.RetrieveUpdateAPIView):
    """Aktuell eingeloggten User holen oder ändern
    
    api/users/about

    curl http://127.0.0.1:8000/api/users/about -H "Authorization: Token 044f242ea137e2d0dc3a2a51d786cc8921cf179f"
    curl -X PATCH -d "user_name='Paul Breitner'"  http://127.0.0.1:8000/api/users/about -H "Authorization: Token 044f242ea137e2d0dc3a2a51d786cc8921cf179f"
    """
    serializer_class = UserSerializer
    authentication_classes = [
                authentication.TokenAuthentication, 
                authentication.SessionAuthentication
    ]  # Wie kann man sich authentifizieren?
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_object(self):
        # holt den aktuell eingeloggten User
        return self.request.user
