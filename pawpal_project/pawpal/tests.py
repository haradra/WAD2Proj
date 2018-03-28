# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import timezone
from pawpal.forms import *
from pawpal.models import *
from pawpal.views import *
from pawpal.urls import *


# helper methods to create user personas
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


# The following tests check whether the urls are loaded/found successfully given the correct conditions/slugs
class PawPalUrlsTests(TestCase):

    def test_my_account(self):
        response = self.client.get(reverse('myaccount'))
        self.assertEqual(response.status_code, 302)

    def test_edit_account_details(self):
        response = self.client.get(reverse('editaccountdetails'))
        self.assertEqual(response.status_code, 302)

    def test_edit_account(self):
        response = self.client.get(reverse('editaccount'))
        self.assertEqual(response.status_code, 302)

    def test_settings(self):
        response = self.client.get(reverse('settings'))
        self.assertEqual(response.status_code, 302)

    def test_password(self):
        response = self.client.get(reverse('password'))
        self.assertEqual(response.status_code, 302)

    # def test_login(self):
    #    add_pet('Tusia','tusia1234@gmail.com','DifficultPassword1')
    #    response = self.client.get(reverse('/pawpal/login/')
    #    self.assertEqual(response.status_code, 302)
