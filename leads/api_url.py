from django.urls import path, include
from rest_framework.routers import DefaultRouter

from leads import api_viewsets

router = DefaultRouter()
router.register(r'agents', api_viewsets.AgentsViewSet, basename="agents")
router.register(r'leads', api_viewsets.LeadsViewSet, basename="leads")

urlpatterns = [
    path('', include(router.urls)),
]
