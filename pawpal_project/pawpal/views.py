# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render

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
