# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime
from pawpal.models import UserProfile, Pet, Rating, Messages
from pawpal.forms import PetForm, UserForm, UserProfileForm


# Create your views here.
def home(request):
    context_dict = {}
#    return HttpResponse("""Home page. PawPal
#    <br/> <a href='/pawpal/about/'>About</a>
#    <br/> <a href='/pawpal/contact/'>Contact us</a>
#    <br/> <a href='/pawpal/editaccount/'>Edit account</a>
#    <br/> <a href='/pawpal/register/'>Register page</a>
#    <br/> <a href='/pawpal/login/'>Login page</a>
#    <br/> <a href='/pawpal/pets/'>Pets page</a>
#    <br/> <a href='/pawpal/messenger/'>Messenger page</a>
#    <br/> <a href='/pawpal/chosenpet/'>Chosen pet page</a>
#    <br/> <a href='/pawpal/myaccount/'>My account page</a>""")
    return render(request, 'pawpal/home.html', context=context_dict)

def about(request):
    return HttpResponse("""About page
    <a href="/pawpal/">home</a>""")
def contact(request):
    return HttpResponse("""Contact page
    <a href="/pawpal/">home</a>""")
def login(request):
    return HttpResponse("""Login page
    <a href="/pawpal/">home</a>""")
def register(request):
    return HttpResponse("""Register page
    <a href="/pawpal/">home</a>""")
def pets(request):
    return HttpResponse("""Pets page
    <a href="/pawpal/">home</a>""")
def editaccount(requst):
    return HttpResponse("""Edit account page
    <a href="/pawpal/">home</a>""")
def messenger(request):
    return HttpResponse("""Messenger page
    <a href="/pawpal/">home</a>""")
def chosenpet(requst):
    return HttpResponse("""Chosen pet page
    <a href="/pawpal/">home</a>""")
def myaccount(requst):
    return HttpResponse("""My account page
    <a href="/pawpal/">home</a>""")
