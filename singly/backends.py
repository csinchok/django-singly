import requests

from django.contrib.auth.models import User

from singly.models import SinglyProfile

class SinglyBackend(object):
    def authenticate(self, code=None):
        data = {
            'code': code,
            'client_id': settings.SINGLY_CLIENT_ID,
            'client_secret': settings.SINGLY_CLIENT_SECRET
        }
        response = requests.get('https://api.singly.com/oauth/access_token', data)
        if response.status_code == 200:
            access_token = response.json.get('access_token')
            account = response.json.get('account')
            try:
                user = SinglyProfile.objects.get(account=account, access_token=access_token).user
            except SinglyProfile.DoesNotExist:
                user = User(username=account)
                user.save()
                SinglyProfile.objects.create(user=user, account=account, access_token=access_token)
                return user
        return None