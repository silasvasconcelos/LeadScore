from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema


from leads import models, serializers


class LeadsViewSet(viewsets.ModelViewSet):
    queryset = models.Lead.objects.all()
    serializer_class = serializers.LeadsSerializer

    @swagger_auto_schema(
        operation_description='Listing all leads in the system.',
        operation_summary='Listing of leads',
        operation_id='list_leads',
        tags=['Leads', ],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description='Detail of lead',
        operation_summary='Detail of lead',
        operation_id='retrieve_lead',
        tags=['Leads', ],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description='Register a new lead.',
        operation_summary='Register lead',
        operation_id='create_lead',
        tags=['Leads', ],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description='Update existing lead.',
        operation_summary='Update lead',
        operation_id='update_lead',
        tags=['Leads', ],
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description='Update specific lead data.',
        operation_summary='Update partial lead',
        operation_id='partial_update_lead',
        tags=['Leads', ],
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description='Delete a lead.',
        operation_summary='Delete lead',
        operation_id='destroy_lead',
        tags=['Leads', ],
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)