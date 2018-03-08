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
from pawpal.forms import ########################import forms here######################


# Create your views here.
def home(request):
    return HttpResponse("Home")
def about(request):
    return HttpResponse("About us")
def contact(request):
    return HttpResponse("Contact us")
def login(request):
    return HttpResponse("Login")
def signup(request):
    return HttpResponse("Sign up")
def pets(request):
    return HttpResponse("Pets")
