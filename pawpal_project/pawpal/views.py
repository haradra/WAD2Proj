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
def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:

                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:

                return HttpResponse("Your PawPal account is disabled.")
        else:

            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:

        return render(request, 'pawpal/login.html', {})

    return HttpResponse("""Login page
    <a href="/pawpal/">home</a>""")
def register(request):
    
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                profile.save()
                registered = True
            else:
                print(user_form.errors, profile_form.errors)
    else:
    	
        user_form = UserForm()
        profile_form = UserProfileForm()
    #When template is ready uncomment this block    
    """
    return render(request,
                  'pawpal/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered
                  })
    """
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
def chosenpet(request):
    return HttpResponse("""Chosen pet page
    <a href="/pawpal/">home</a>""")
def myaccount(request):
    return HttpResponse("""My account page
    <a href="/pawpal/">home</a>""")

