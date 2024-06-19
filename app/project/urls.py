from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include("user.api.urls")),
    path('api/events/', include("events.api.urls")),
    path(
        "schema/",
        SpectacularAPIView.as_view(api_version="v2"),
        name="schema",
    ),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + [
        path("__debug__/", include("debug_toolbar.urls")),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

