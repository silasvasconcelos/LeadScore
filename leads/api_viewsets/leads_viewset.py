from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from core.pagination import PageNumberWithLimitPagination
from leads import models, serializers


class LeadsViewSet(viewsets.ModelViewSet):
    queryset = models.Lead.objects.all()
    queryset_agens = models.Agent.objects.all()
    serializer_class = serializers.LeadsSerializer
    lead_support_serializer = serializers.LeadSupportSerializer
    pagination_class = PageNumberWithLimitPagination

    def get_serializer_class(self):
        return {
            'agents': self.lead_support_serializer,
            'agents_last_lead': self.lead_support_serializer,
        }.get(self.action, self.serializer_class)

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

    @swagger_auto_schema(
        operation_description='Listing all agents available for lead.',
        operation_summary='Listing all agents available for lead',
        operation_id='agents',
        tags=['Leads', ],
    )
    @action(detail=True, methods=['GET'])
    def agents(self, request, *args, **kwargs):
        lead = self.get_object()
        agents = self.filter_queryset(self.queryset_agens.lead_score(lead.pk))
        serializer = self.get_serializer(agents, many=True, context={'lead': lead})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description='Listing all agents available for last lead.',
        operation_summary='Listing all agents available for last lead',
        operation_id='agents_last_lead',
        tags=['Leads', ],
    )
    @action(detail=False, methods=['GET'], url_path='agents')
    def agents_last_lead(self, request, *args, **kwargs):
        lead = self.queryset.last()
        agents = self.filter_queryset(self.queryset_agens.lead_score(lead.pk))
        serializer = self.get_serializer(agents, many=True, context={'lead': lead})
        return Response(serializer.data, status=status.HTTP_200_OK)
