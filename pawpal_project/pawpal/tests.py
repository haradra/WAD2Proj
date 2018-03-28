# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.test import TestCase
from pawpal.forms import *
from pawpal.models import *
from pawpal.views import *
from pawpal.urls import *
from django.conf import settings
import os

# Helper methods to create user personas
def add_user(username, email, password):
    u = UserProfile.objects.get_or_create(user=username)[0]
    u.email = email
    u.password = password
    u.save()
    return u

# Helper method to create pet
def add_pet(username, email, password):
    u = PetProfile.objects.get_or_create(user=username)[0]
    u.email = email
    u.password = password
    u.save()
    return u

# Helper method to create an admin
def create_admin():
    u = UserProfile.objects.get_or_create(username="testadmin", is_staff=True)
    u.save()


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

    # Checks if a proper message is displayed
    def test_home_displays_welcome_message(self):
        response = self.client.get(reverse('home'))
        self.assertIn("Welcome to PawPal!".lower(), response.content.decode('ascii').lower())

    # Checks if base template is recognised
    def test_contact_page_using_template(self):
        response = self.client.get(reverse('contact'))
        self.assertTemplateUsed(response, 'base.html')

class HomeViewTests(TestCase):
    # Return a success status code if home page loads
    def test_home_view_loads_successfully(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    # Return a success status code if about page loads
    def test_about_view_loads_successfully(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    # Return a success status code if contact us page loads
    def test_contactus_view_loads_successfully(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    # Return a success status code if register page loads
    def test_register_view_loads_successfully(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    # Return a success status code if login page loads
    def test_login_view_loads_successfully(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

class ModelTests(TestCase):

    def setUp(self):
        try:
            from population_script import populate
            populate()
        except ImportError:
            print('The module population_script does not exist')
        except NameError:
            print('The function populate() does not exist or is not correct')
        except:
            print('Something went wrong in the populate() function')

