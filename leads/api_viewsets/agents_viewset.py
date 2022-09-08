from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema


from leads import models, serializers


class AgentsViewSet(viewsets.ModelViewSet):
    queryset = models.Agent.objects.all()
    serializer_class = serializers.AgentsSerializer

    @swagger_auto_schema(
        operation_description='Listing all agents in the system.',
        operation_summary='Listing of agents',
        operation_id='list_agents',
        tags=['Agents', ],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description='Detail of agent',
        operation_summary='Detail of agent',
        operation_id='retrieve_agent',
        tags=['Agents', ],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description='Register a new agent.',
        operation_summary='Register agent',
        operation_id='create_agent',
        tags=['Agents', ],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description='Update existing agent.',
        operation_summary='Update agent',
        operation_id='update_agent',
        tags=['Agents', ],
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description='Update specific agent data.',
        operation_summary='Update partial agent',
        operation_id='partial_update_agent',
        tags=['Agents', ],
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description='Delete a agent.',
        operation_summary='Delete agent',
        operation_id='destroy_agent',
        tags=['Agents', ],
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)