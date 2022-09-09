from rest_framework import serializers

from leads import models


class LeadSupportSerializer(serializers.ModelSerializer):
    score = serializers.IntegerField(help_text="Score of the Lead", read_only=True)

    class Meta:
        model = models.Agent
        fields = ('id', 'name', 'level', 'score', 'created_at',)
        read_only_fields = ('id', 'score', 'created_at',)
