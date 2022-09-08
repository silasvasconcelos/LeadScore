from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .settings_drf import schema_view

urlpatterns_api_v1 = [
    path('', include('leads.api_url')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema_json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema_swagger_ui'),
    re_path(r'^$', schema_view.with_ui('redoc', cache_timeout=0), name='schema_redoc'),
    path('api/v1/', include(urlpatterns_api_v1)),
]
