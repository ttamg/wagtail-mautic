from django.db import models
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting


@register_setting
class MauticSettings(BaseSetting):
    mautic_url = models.URLField(
        help_text="Your Mautic site URL including the https:// prefix (easiest option)",
        null=True,
        blank=True,
    )

    panels = [
        FieldPanel("mautic_url"),
    ]
