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
    userProfile = {}
    if request.user and request.user.is_authenticated:
        userProfile = UserProfile.objects.get(user=request.user)
    context_dict = {'records_pets':pets,'userProfile':userProfile}
    return render(request, 'pawpal/home.html', context=context_dict)

def about(request):
    userProfile = {}
    if request.user and request.user.is_authenticated:
        userProfile = UserProfile.objects.get(user=request.user)
    return render(request, 'pawpal/about.html',{'userProfile':userProfile})
def contact(request):
    userProfile={}
    if request.user and request.user.is_authenticated:
        userProfile = UserProfile.objects.get(user=request.user)
    return render(request, 'pawpal/contact.html',{'userProfile':userProfile})
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

    if request.user and request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))
    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        pet_form = PetForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profilePicture' in request.FILES:
                profile.profilePicture = request.FILES['profilePicture']
            profile.save()
            login(request,user,backend='django.contrib.auth.backends.ModelBackend')
            registered = True
            return HttpResponseRedirect(reverse('home'))
        elif user_form.is_valid() and pet_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            pet = pet_form.save(commit=False)
            pet.user = user
            if 'petPicture' in request.FILES:
                pet.petPicture = request.FILES['petPicture']
            pet.save()
            login(request,user,backend='django.contrib.auth.backends.ModelBackend')
            registered = True
            return HttpResponseRedirect(reverse('home'))
        else:
            print(user_form.errors, profile_form.errors)
    else:

        user_form = UserForm()
        profile_form = UserProfileForm()
        pet_form = PetForm()

    return render(request,
                  'pawpal/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'pet_form': pet_form,
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

    userProfile = UserProfile.objects.get(user=request.user)
    return render(request, 'pawpal/settings.html', {
        'github_login': github_login,
        'twitter_login': twitter_login,
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect,
        'userProfile': userProfile
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
    userProfile = UserProfile.objects.get(user=request.user)
    return render(request, 'pawpal/password.html', {'form': form,'userProfile':userProfile})
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
    userProfile = UserProfile.objects.get(user=request.user)
    context_dict = {'form':form,'userProfile':userProfile}
    return render(request, 'pawpal/editaccount.html', context=context_dict)

@login_required
def get_user_profile(request, username):
    if request.user and request.user.username == username:
        return HttpResponseRedirect(reverse('myaccount'))
    find_user = User.objects.get(username=username)
    page_to_render=""
    try:
        user = UserProfile.objects.get(user=find_user)
        page_to_render = "pawpal/user_profile.html"
    except:
        user = Pet.objects.get(user=find_user)
        page_to_render = "pawpal/pet_profile.html"
    userProfile = UserProfile.objects.get(user=request.user)
    return render(request, page_to_render, {"user":user,"rating":2,"ratings":range(1,6),"userProfile":userProfile})
@login_required
def myaccount(request):
    user = UserProfile.objects.get(user=request.user)
    userProfile = UserProfile.objects.get(user=request.user)
    return render(request, 'pawpal/myaccount.html', {"user":user,"rating":2,"ratings":range(1,6),"userProfile":userProfile})
