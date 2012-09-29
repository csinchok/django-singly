# -*- coding: utf-8 -*-
from django.db import models

from django.contrib.auth.models import User

class SinglyProfile(models.Model):
    user = models.OneToOneField(User, related_name='singly')
    access_token = models.CharField(max_length=255)
    account = modles.CharField(max_length=255)
    