# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash, authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm, UserCreationForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime
from django.contrib import messages
from pawpal.models import UserProfile, Pet, Rating, Messages, User
from pawpal.forms import PetForm, UserForm, UserProfileForm, UpdateProfile
from social_django.models import UserSocialAuth

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
    context_dict = {}
    
    pets = Pet.objects.order_by('name')
    
    context_dict = {'records_pets':pets}
    return render(request, 'pawpal/home.html', context=context_dict)

def about(request):
    return render(request, 'pawpal/about.html')
def contact(request):
    return render(request, 'pawpal/contact.html')
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

                return HttpResponse("Your PawPal account is not active.")
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
            print(request.FILES['profilePicture'])
            if 'profilePicture' in request.FILES:
                print("doing job")
                print(profile.profilePicture)
                profile.profilePicture = request.FILES['profilePicture']
                print(profile.profilePicture)
            profile.save()
            print(profile)
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:

        user_form = UserForm()
        profile_form = UserProfileForm()


    return render(request,
                  'pawpal/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered
                  })
    """
    return HttpResponse("Register page<a href="/pawpal/">home</a>")
    """
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
@login_required
def settings(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'pawpal/settings.html', {
        'github_login': github_login,
        'twitter_login': twitter_login,
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })

@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'pawpal/password.html', {'form': form})
def pets(request):
    return HttpResponse("""Pets page
    <a href="/pawpal/">home</a>""")
@login_required
def editaccount(request):
    context_dict = {}
    user = request.user
    if request.method == 'POST':
        form = UpdateProfile(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myaccount'))
    else:
        form = UpdateProfile()

    context_dict = {'form':form}
    return render(request, 'pawpal/editaccount.html', context=context_dict)

@login_required
def get_user_profile(request, username):
    user = UserProfile.objects.get(user=request.user)
    return render(request, 'pawpal/user_profile.html', {"user":user})
@login_required
def messenger(request):
    return HttpResponse("""Messenger page
    <a href="/pawpal/">home</a>""")
def chosenpet(request):
    return render(request, 'pawpal/chosenpet.html',{})
@login_required
def myaccount(request):
    user = UserProfile.objects.get(user=request.user)
    return render(request, 'pawpal/myaccount.html', {"user":user})
