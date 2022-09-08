from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from core.utils import env

schema_view = get_schema_view(
    openapi.Info(
        title="LeadScore API",
        default_version='v1',
        description="API to helper sellers to find and filter customers",
        contact=openapi.Contact(email="silasvasconcelos@hotmail.com.br"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

SECURITY_DEFINITIONS = {
    'Bearer': {
        'type': 'apiKey',
        'name': 'Authorization',
        'in': 'header'
    }
}

DEFAULT_AUTHENTICATION_CLASSES = [
    'rest_framework_simplejwt.authentication.JWTAuthentication',
]

if env.bool('ENABLE_BASIC_LOGIN', default=False):
    SECURITY_DEFINITIONS.update({
        'Basic': {
            'type': 'basic',
        },
    })
    DEFAULT_AUTHENTICATION_CLASSES.append(
        'rest_framework.authentication.BasicAuthentication')

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': DEFAULT_AUTHENTICATION_CLASSES,
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        "rest_framework.permissions.IsAuthenticated",
        "rest_framework.permissions.DjangoModelPermissions",
    ],
    'DEFAULT_PAGINATION_CLASS': 'core.pagination.PageNumberWithLimitPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter'
    ],
}

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': SECURITY_DEFINITIONS
}
