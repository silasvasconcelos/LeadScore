from django_filters import rest_framework as filters

from leads import models


class LeadsFilters(filters.FilterSet):
    score = filters.NumberFilter(help_text="Filter the agents by score")

    class Meta:
        model = models.Agent
        fields = ('name', 'score',)
