from django import template

# from wagtail_mautic.models import MauticSettings

register = template.Library()


@register.inclusion_tag("wagtail_mautic/mautic_tracking.html")
def mautic_tracking():
    return {}
