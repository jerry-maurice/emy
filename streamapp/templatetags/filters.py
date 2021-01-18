from django import template
from django.utils.html import format_html, escape
from django.utils.timesince import timesince
from datetime import *
from django.utils.timezone import utc


register = template.Library()

@register.filter(name='time_difference')
def time_difference(value):
    now = datetime.utcnow().replace(tzinfo=utc)
    try:
        difference = now - value
    except:
        return value

    if difference <= timedelta(minutes=1):
        return 'Just now'
    return '%(time)s ago' % {'time': timesince(value).split(', ')[0]}