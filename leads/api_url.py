from django.urls import path, include
from rest_framework.routers import DefaultRouter

from leads import api_viewsets

router = DefaultRouter()
router.register(r'agents', api_viewsets.AgentsViewSet, basename="agents")

urlpatterns = [
    path('', include(router.urls)),
]
