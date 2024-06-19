from django.urls import path
from . import views


urlpatterns = [
    path("categories", views.CategoryListCreateView.as_view(), name="list-categories"),
    path("external", views.ExternalAPIView.as_view(), name="extern"),
]