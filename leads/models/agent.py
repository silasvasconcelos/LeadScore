from django.db import models
from django.utils.translation import gettext_lazy as _


from .managers import AgentManager

class Agent(models.Model):
    name = models.CharField(_("Name"), max_length=200, help_text="Name of the agent")
    level = models.FloatField(_("Level"), help_text="Level of the agent")
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True, null=True, editable=False)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True, null=True, editable=False)

    objects = AgentManager()
    class Meta:
        verbose_name = _("Agent")
        verbose_name_plural = _("Agents")

    def __unicode__(self):
        return self.name
