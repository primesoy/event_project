from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from . import views

app_name = "user"   # {% url 'user:list-user' %}

urlpatterns = [
    path("", views.ListUserView.as_view(), name="list-user"),
    path("create", views.UserCreateView.as_view(), name="create-user"),
    path("about", views.ManageUserView.as_view(), name="manage-user"),
    path("token", obtain_auth_token, name="token"),  # obtain_auth_token(request)
    # http://127.0.0.1/api/users/confirm/9/493ca595-2caf-11ef-a405-50ebf6b8f447
    path("confirm/<int:uid>/<str:token>", views.EmailConfirmationUserView.as_view(), name="confirm-user"),
]