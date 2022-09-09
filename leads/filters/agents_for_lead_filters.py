from django_filters import rest_framework as filters

from leads import models


class AgentsForLeadFilters(filters.FilterSet):
    score = filters.NumberFilter(help_text="Filter the agents by score")
    score_gte = filters.NumberFilter(field_name="score", lookup_expr="gte",
                                     help_text="Filter the agents by score greater than or equal to the score")
    score_lte = filters.NumberFilter(field_name="score", lookup_expr="lte",
                                     help_text="Filter the agents by score lower than or equal to the score")

    class Meta:
        model = models.Agent
        fields = ('name', 'score', 'score_gte', 'score_lte',)
