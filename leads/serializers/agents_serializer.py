from rest_framework import serializers

from leads import models


class AgentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Agent
        fields = ('id', 'name', 'level')
        read_only_fields = ('id',)
