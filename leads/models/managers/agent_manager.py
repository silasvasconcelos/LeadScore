from datetime import datetime

from django.db import models
from django.utils import timezone

from leads import models as leads_models


class AgentQuerySet(models.QuerySet):
    def lead_score(self, lead_id):
        _timezone = timezone.get_current_timezone()
        now = datetime.now(_timezone)
        start_hour = 9
        end_hour = 18
        # TODO: the normal values is 3600 seconds to one hour and 60 seconds to one minute, this is only for Sqlite databse
        base_to_day = 86400000000
        base_to_hour = 3600000000

        lead_qs = leads_models.Lead.objects.filter(pk=lead_id).values('created_at')[:1]
        return leads_models.Agent.objects.annotate(
            now=models.functions.Cast(models.Value(now), output_field=models.DateTimeField()),
            lead_created_at=lead_qs,
            diff=models.functions.Cast(now - models.F('lead_created_at'), output_field=models.FloatField()),
            days=models.functions.Cast(models.F('diff') / models.Value(base_to_day),
                                       output_field=models.IntegerField()),
            prev_hours=models.functions.Cast(models.F('diff') / models.Value(base_to_hour),
                                             output_field=models.IntegerField()),
            hours=models.Case(
                models.When(now__hour__gt=end_hour, then=models.Value(8)),
                models.When(now__hour__gt=start_hour, now__hour__lt=end_hour, then=models.F('now__hour') - start_hour),
                models.When(prev_hours__gt=8, then=models.Value(8)),
                default=models.F('prev_hours')
            ),
            total_hours=(models.Value(8) * models.F('days')) + models.F('hours'),
            score=models.functions.Cast(models.Case(
                models.When(total_hours__lte=0, then=models.F('level')),
                default=models.F('total_hours') * models.F('level')), output_field=models.IntegerField())
        )


class AgentManager(models.Manager):
    def get_queryset(self):
        return AgentQuerySet(self.model, using=self._db)

    def lead_score(self, lead_id):
        return self.get_queryset().lead_score(lead_id)
