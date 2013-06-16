from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def sep(v):
    """Replace the , by a ."""

    return v.replace(',','.')

