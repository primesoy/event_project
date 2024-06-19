from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include("user.api.urls")),
    path('api/events/', include("events.api.urls")),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + [
        path("__debug__/", include("debug_toolbar.urls")),
    ]

