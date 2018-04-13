from django import template
from django.urls import reverse

from tickets.core.middlewares import get_current_request

register = template.Library()


@register.simple_tag
def is_active(url):
    request = get_current_request()
    # Main idea is to check if the url and the current path is a match
    if request.path == reverse(url):
        return "active"

    return ""
