from rest_framework import serializers

from leads import models


class LeadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lead
        fields = ('id', 'name', 'phone', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at',)
