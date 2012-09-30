import requests

from django.contrib.auth.models import User
from django.conf import settings

from singly.models import SinglyProfile

class SinglyBackend(object):
    
    supports_inactive_user = False
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def authenticate(self, code=None):
        params = {
            'code': code,
            'client_id': settings.SINGLY_CLIENT_ID,
            'client_secret': settings.SINGLY_CLIENT_SECRET
        }
        response = requests.post('https://api.singly.com/oauth/access_token', data=params)
        if response.status_code == 200:
            access_token = response.json.get('access_token')
            account = response.json.get('account')
            try:
                user = SinglyProfile.objects.get(account=account).user
                user.access_token = access_token
                user.save()
                return user
            except SinglyProfile.DoesNotExist:
                profile_response = requests.get("https://api.singly.com/v0/profile", params={'access_token': access_token})
                user_kwargs = {'username': account}
                if profile_response.status_code == 200:
                    if 'email' in profile_response.json:
                        user_kwargs['username'] = profile_response.json['email']
                    elif 'name' in profile_response.json:
                        user_kwargs['username'] = profile_response.json['name'].lower().replace(' ', '')
                    if profile_response.json.get('name'):
                        try:
                            user_kwargs['first_name'], user_kwargs['last_name'] = profile_response.json['name'].split(' ')
                        except IndexError:
                            pass
                    user_kwargs['email'] = profile_response.json.get('email')
                user = User(**user_kwargs)
                user.save()
                SinglyProfile.objects.create(user=user, account=account, access_token=access_token)
                return user
        return None