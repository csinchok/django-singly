from django.conf import settings

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponseBadRequest

def callback(request):
    if 'error' in request.GET:
        return request.GET['error']
    code = request.GET.get('code')
    if code:
        user = authenticate(code=code)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(getattr(settings, 'SINGLY_CALLBACK_REDIRECT', '/'))
    return HttpResponseBadRequest('Login failed.')