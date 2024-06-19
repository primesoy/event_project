from project.settings.base import *


# REST Framework
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        # "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated"
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Event Manager API',
    'DESCRIPTION': 'Django Event manager',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SWAGGER_UI_DIST': 'SIDECAR',
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    # 'SERVE_AUTHENTICATION': ['rest_framework.authentication.SessionAuthentication'],
    # 'SERVE_PERMISSIONS': ['rest_framework.permissions.IsAuthenticated'],

    # OTHER SETTINGS
}


INSTALLED_APPS.extend(
    [
        "debug_toolbar"
    ]
)

MIDDLEWARE.extend(
    [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]
)

INTERNAL_IPS = [
    "127.0.0.1",
]