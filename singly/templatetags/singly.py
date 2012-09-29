from django import template
from django.conf import settings
from django.core.urlresolvers import reverse

from ..views import callback

register = template.Library()

@register.simple_tag(takes_context=True)
def singly_login_url(context, service):
    redirect_uri = getattr(settings, 'SINGLY_CALLBACK_URL', None)
    if redirect_uri is None:
        redirect_uri = "http://%s%s" % (context['request'].get_host(), reverse(callback, current_app='singly'))
    auth_url = "https://api.singly.com/oauth/authorize?client_id=%s&redirect_uri=%s&service=%s" % (
        getattr(settings, 'SINGLY_CLIENT_ID', None),
        redirect_uri,
        service
    )
    if hasattr(context['user'], 'singly'):
        auth_url = "%s&account=%s" % (auth_url, context['user'].singly.account)
    return auth_url