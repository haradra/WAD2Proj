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
from django.conf import settings
import os

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

class TemplateTests(TestCase):
    # Checks whether the base template exists
    def test_base_template_exists(self):
        path_to_base = os.path.join(settings.TEMPLATE_DIR, 'base.html')
        self.assertTrue(os.path.isfile(path_to_base))

    def test_link_to_home_in_base_template(self):
        response = self.client.get(reverse('home'))
        self.assertIn(reverse('home'), response.content.decode('ascii'))

    def test_home_displays_welcome_message(self):
        # Checks if a proper message is displayed
        response = self.client.get(reverse('home'))
        self.assertIn("Welcome to PawPal!".lower(), response.content.decode('ascii').lower())

    def test_contact_page_using_template(self):
        # Checks if base template is recognised
        response = self.client.get(reverse('contact'))
        self.assertTemplateUsed(response, 'base.html')

class ModelTests(TestCase):

    def setUp(self):
        try:
            from populate_pawpal import populate
            populate()
        except ImportError:
            print('The module populate_pawpal does not exist')
        except NameError:
            print('The function populate() does not exist or is not correct')
        except:
            print('Something went wrong in the populate() function')

    #def test_login(self):
    #    add_pet('Tusia','tusia1234@gmail.com','DifficultPassword1')
    #    response = self.client.get(reverse('/pawpal/login/')
    #    self.assertEqual(response.status_code, 302)
