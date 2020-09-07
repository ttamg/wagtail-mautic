from django import template
from wagtail_mautic.models import MauticSettings

register = template.Library()


@register.inclusion_tag("mautic_tracking.html")
def mautic_tracking():
    if MauticSettings.mautic_url:
        return {"tracking": True, "url": MauticSettings.mautic_url}
    else:
        return {"tracking": False}
