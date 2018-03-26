# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
def add_user(username, email, password):
    u = UserProfile.objects.get_or_create(user=username)[0]
    u.email = email
    u.password = password
    u.save()
    return u

def add_pet(username, email, password):
    u = Pet.objects.get_or_create(user=username)[0]
    u.email = email
    u.password = password
    u.save()
    return u
