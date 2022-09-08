from rest_framework import serializers

from leads import models


class AgentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Agent
        fields = ('id', 'name', 'level', 'created_at', 'updated_at',)
        read_only_fields = ('id', 'created_at', 'updated_at',)
