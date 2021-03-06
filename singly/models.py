import json
from django.db import models

from django.contrib.auth.models import User

class SinglyProfile(models.Model):
    user = models.OneToOneField(User, related_name='singly')
    access_token = models.CharField(max_length=512)
    account = models.CharField(max_length=255)
    profile = models.TextField()
    
    def services(self):
        profile = json.loads(self.profile)
        return profile['services'].keys()
    
    def __unicode__(self):
        return "Profile for '%s'" % self.user