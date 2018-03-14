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
from pawpal.forms import PetForm, UserForm, UserProfileForm
from social_django.models import UserSocialAuth
from django.db.models import Avg

# Create your views here.
def home(request):
    context_dict = {}
    rates = Rating.objects.order_by('pet')
    pets = Pet.objects.order_by('name')
    users = User.objects.order_by('user').annotate(
        avg_friendliness=Avg('rating__friendliness'),
        avg_good_w_pets=Avg('rating__good_w_pets'),
        avg_trust=Avg('rating__trust'),
        )
    context_dict = {'records_user': users,'records_pets':pets, 'rates':rates}
    
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
    return render(request, 'pawpal/about.html')
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
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                profile.save()
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
def editaccount(requst):
    return HttpResponse("""Edit account page
    <a href="/pawpal/">home</a>""")
@login_required
def messenger(request):
    return HttpResponse("""Messenger page
    <a href="/pawpal/">home</a>""")
def chosenpet(request):
    return HttpResponse("""Chosen pet page
    <a href="/pawpal/">home</a>""")
@login_required
def myaccount(request):
    return HttpResponse("""My account page
    <a href="/pawpal/">home</a>""")

