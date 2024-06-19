from django.urls import path
from . import views


urlpatterns = [
    path("", views.EventListCreateView.as_view(), name="event-list"),
    path("<int:pk>", views.EventRetrieveUpdateView.as_view(), name="event-update-create"),
    path("categories", views.CategoryListCreateView.as_view(), name="list-categories"),
    path("external", views.ExternalAPIView.as_view(), name="extern"),
    path("mtypes", views.MachineTypeListView.as_view(), name="list-machinetypes"),
]