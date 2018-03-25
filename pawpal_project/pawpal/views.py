# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash, authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm, UserCreationForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from pawpal.models import UserProfile, Pet, Rating, Messages, User
from pawpal.forms import *
from social_django.models import UserSocialAuth
from django_private_chat.models import Dialog
from django.db.models import Q

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

    userProfile = {}
    listedProfiles = {}
    userType="user"
    if request.user and request.user.is_authenticated:
        try:
            userProfile = UserProfile.objects.get(user=request.user)
            listedProfiles = Pet.objects.order_by('name')
            userType="user"
        except:
            try:
                userProfile = Pet.objects.get(user=request.user)
                listedProfiles = UserProfile.objects.order_by('description')
                userType="pet"
            except:
                userProfile = UserProfile.objects.get_or_create(user=request.user)[0]
                listedProfiles = Pet.objects.order_by('name')
                userType="user"
    else:
        listedProfiles = Pet.objects.order_by('name')
        userType="user"
    context_dict = {'listed_profiles':listedProfiles,'userProfile':userProfile,"userType":userType}
    return render(request, 'pawpal/home.html', context=context_dict)

def about(request):
    userProfile = {}
    if request.user and request.user.is_authenticated:
        try:
            userProfile = UserProfile.objects.get(user=request.user)
        except:
            try:
                userProfile = Pet.objects.get(user=request.user)
            except:
                userProfile = UserProfile.objects.get_or_create(user=request.user)[0]
    return render(request, 'pawpal/about.html',{'userProfile':userProfile})

def contact(request):
    userProfile={}
    if request.user and request.user.is_authenticated:
        try:
            userProfile = UserProfile.objects.get(user=request.user)
        except:
            try:
                userProfile = Pet.objects.get(user=request.user)
            except:
                userProfile = UserProfile.objects.get_or_create(user=request.user)[0]
    return render(request, 'pawpal/contact.html',{'userProfile':userProfile})

def user_login(request):
    login_error = False
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.error(request,'Username or password not correct')
            return HttpResponseRedirect(reverse('home'))

    else:

        return render(request, 'pawpal/login.html', {})

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
            if 'profilePicture' in request.FILES:
                pet.profilePicture = request.FILES['profilePicture']
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

    try:
        userProfile = UserProfile.objects.get(user=request.user)
    except:
        try:
            userProfile = Pet.objects.get(user=request.user)
        except:
            userProfile = UserProfile.objects.get_or_create(user=request.user)[0]
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
    try:
        userProfile = UserProfile.objects.get(user=request.user)
    except:
        try:
            userProfile = Pet.objects.get(user=request.user)
        except:
            userProfile = UserProfile.objects.get_or_create(user=request.user)[0]
    return render(request, 'pawpal/password.html', {'form': form,'userProfile':userProfile})


@login_required
def editaccountdetails(request):
    print (request.readlines())
    # This is really bad code, but it works for now
    if request.method == 'POST':
        try:
            Pet.objects.get(user=request.user)
            form = UpdatePetProfile(data=request.POST, instance = Pet.objects.get(user=request.user))
        except Pet.DoesNotExist:
            form = UpdateUserProfile(data=request.POST, instance= UserProfile.objects.get(user=request.user))
        finally:
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                if 'profilePicture' in request.FILES:
                    profile.profilePicture = request.FILES['profilePicture']
                profile.save()
                login(request, request.user, backend='django.contrib.auth.backends.ModelBackend')
                return HttpResponseRedirect(reverse('myaccount'))
            else:
                print(form.errors)

    else:
        try:
            profile = Pet.objects.get(user=request.user)
            form = UpdatePetProfile(data={'location':profile.location,'species':profile.species,'description':profile.description}, instance= Pet.objects.get(user=request.user))
        except Pet.DoesNotExist:
            profile = UserProfile.objects.get(user=request.user)
            form = UpdateUserProfile(data={'experience':profile.experience, 'description':profile.description, 'dateOfBirth':profile.dateOfBirth, 'location':profile.location}, instance= UserProfile.objects.get(user=request.user))
    try:
        #Pet.objects.get(user=request.user)
        userProfile = Pet.objects.get(user=request.user)
    except Pet.DoesNotExist:
        userProfile = UserProfile.objects.get(user=request.user)

    context_dict = {'form': form, 'userProfile': userProfile}
    return render(request, 'pawpal/editaccountdetails.html', context=context_dict)


@login_required
def editaccount(request):
    #This is really bad code, but it works for now
    if request.method == 'POST':
        try:
            Pet.objects.get(user=request.user)
            user_form = UpdateUserPet(data=request.POST, instance=request.user)
        except Pet.DoesNotExist:
            user_form= UpdateUserSeeker(data=request.POST, instance=request.user)
        finally:
            if user_form.is_valid():
                user = user_form.save()
                user.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return HttpResponseRedirect(reverse('myaccount'))
            else:
                print(user_form.errors)
    else:
        try:
            Pet.objects.get(user=request.user)
            user_form = UpdateUserPet(data=request.POST, instance=request.user)
        except Pet.DoesNotExist:
            user_form= UpdateUserSeeker(data=request.POST, instance=request.user)
    try:
        Pet.objects.get(user=request.user)
        userProfile = Pet.objects.get(user=request.user)
    except Pet.DoesNotExist:
        userProfile = UserProfile.objects.get(user=request.user)
        
        """
        if hasattr(user, 'Pet'):
            form = UpdateUserProfile(request.POST, instance=user)
        elif hasattr(user, 'UserProfile'):
            form = UpdatePetProfile(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myaccount'))
    else:
        if hasattr(user, 'Pet'):
            form = UpdateUserProfile(request.POST, instance=user)
        elif hasattr(user, 'UserProfile'):
            form = UpdatePetProfile(request.POST, instance=user)
            
    if hasattr(user, 'Pet'):
        userProfile = UserProfile.objects.get(user=request.user)
    elif hasattr(user, 'UserProfile'):
        userProfile = Pet.objects.get(user=request.user)
    """
        
    context_dict = {'user_form':user_form, 'userProfile':userProfile}
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
    try:
        userProfile = UserProfile.objects.get(user=request.user)
    except:
        try:
            userProfile = Pet.objects.get(user=request.user)
        except:
            userProfile = UserProfile.objects.get_or_create(user=request.user)[0]
    ratings = Rating.objects.filter(toWho=find_user)
    if len(ratings) > 0:
        number_of_ratings = len(ratings)
        rating = float(format(sum([int(i.rating) for i in ratings]) / number_of_ratings, '.2f'))
    else:
        rating, number_of_ratings = 0, 0

    try:
        madeBy_user_rating = int(Rating.objects.get(toWho=find_user, madeBy=request.user).rating)
    except:
        madeBy_user_rating = 0
    return render(request, page_to_render, {"user":user,"rating":rating,"ratings":range(1,6),
                                            "userProfile":userProfile, "madeBy_user_rating":madeBy_user_rating,
                                            "number_of_ratings":number_of_ratings})

@login_required
def myaccount(request):
    try:
        userProfile = UserProfile.objects.get(user=request.user)
        last_login = userProfile.user.last_login
    except:
        try:
            userProfile = Pet.objects.get(user=request.user)
            last_login = userProfile.user.last_login
        except:
            userProfile = UserProfile.objects.get_or_create(user=request.user)[0]
            last_login = userProfile.user.last_login
    ratings = Rating.objects.filter(toWho=request.user)
    if len(ratings) > 0:
        number_of_ratings = len(ratings)
        rating = float(format(sum([int(i.rating) for i in ratings]) / number_of_ratings, '.2f'))
    else:
        rating, number_of_ratings = 0, 0
    chats=Dialog.objects.filter(Q(owner=request.user)|Q(opponent=request.user))
    new_chats=[]
    for chat in chats:
        user = None
        if chat.owner == request.user:
            user = chat.opponent
        else:
            user = chat.owner
        profile = None
        try:
            profile = UserProfile.objects.get(user=user)
        except:
            try:
                profile = Pet.objects.get(user=user)
            except:
                profile = UserProfile.objects.get_or_create(user=user)[0]
        new_chats.append(profile)
    return render(request, 'pawpal/myaccount.html', {"chats":new_chats,"user":userProfile,"rating":rating,"ratings":range(1,6),
                                                     "userProfile":userProfile, "number_of_ratings":number_of_ratings, "last_login":last_login})


@login_required
def create_rating(request, username, rating):
    if not (username and rating):
        return HttpResponseRedirect(reverse('home'))
    find_user = User.objects.get(username=username)

    rating_object = Rating.objects.get_or_create(madeBy=request.user, toWho=find_user)[0]
    rating_object.rating = int(rating)
    rating_object.save()

    return get_user_profile(request, username)