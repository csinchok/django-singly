from django import template
from django.conf import settings
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag(takes_context=True)
def singly_login_url(context, service):
    redirect_uri = settings.getattr('SINGLY_CALLBACK_URL', None)
    if redirect_uri is None:
        redirect_uri = "%s/%s" % (context['request'].get_host(), reverse('singly:singly_callback'))
    auth_url = "https://api.singly.com/oauth/authorize?client_id=%s&redirect_uri=%s&service=%s" % (
        settings.get('SINGLY_CLIENT_ID'),
        redirect_uri,
        service
    )
    if getattr(context['request']['user'], 'singly'):
        auth_url = "%s&account=%s" % (auth_url, context['request']['user'].singly.account)
    return auth_url