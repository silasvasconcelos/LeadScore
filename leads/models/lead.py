from django.db import models
from django.utils.translation import gettext_lazy as _


class Lead(models.Model):
    name = models.CharField(_("Name"), max_length=200, help_text="Name of the lead")
    phone = models.CharField(_("Phone"), max_length=11, help_text="Number of phone of the agent", unique=True)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    class Meta:
        verbose_name = _("Lead")
        verbose_name_plural = _("Leads")

    def __unicode__(self):
        return self.name
