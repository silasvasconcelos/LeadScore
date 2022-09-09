import re

from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from leads import models


class LeadsSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=20, help_text="Number of phone of the agent")

    class Meta:
        model = models.Lead
        fields = ('id', 'name', 'phone', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at',)

    def validate_phone(self, phone):
        phone_cleaned = re.sub(r'\W', '', phone)

        if len(phone_cleaned) != 11:
            raise serializers.ValidationError({
                "phone": _("The phone must equal (DD) 00000-0000 or 0000000-0000, but must be 11 digits"),
            })
        return phone_cleaned
