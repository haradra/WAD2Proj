import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'pawpal_project.settings')

import django
from django.db import models
django.setup()
from django.conf import settings
from pawpal.models import *
import datetime

def populate():

    users = [
        {"username":"LoveIguanas",
         "password": "IreallyLoveIguanas123456789",
         "first_name":"Donald",
         "last_name": "Duck",
         "last_login": models.DateTimeField(auto_now_add=True),
         "location": "Glasgow",
         "dateOfBirth": datetime.date(1995, 2, 1),
         "profilePicture": models.ImageField(verbose_name="picture"),
         "experience": int(4),
         "description": "I love Iguanas, like really. Iguanas <3",
         "showPets": False,
         },
        {"username": "Doggos",
         "password": "IreallyLoveDoggos123456789",
         "first_name": "Mark",
         "last_name": "Nicold",
         "last_login": models.DateTimeField(auto_now_add=True),
         "location": "Glasgow",
         "dateOfBirth": datetime.date(1995, 2, 1),
         "profilePicture": models.ImageField(verbose_name="picture"),
         "experience": int(8),
         "description": "Doggos, doggos, I have one, let's spend with him all our time!",
         "showPets": True,
         },
        {"username": "anilano",
         "password": "Irsdawnilano123456789",
         "first_name": "Anilano",
         "last_name": "Korton",
         "last_login": models.DateTimeField(auto_now_add=True),
         "location": "Edinburgh",
         "dateOfBirth": datetime.date(1995, 2, 1),
         "profilePicture": models.ImageField(verbose_name="picture", default = settings.MEDIA_ROOT + "1.jpeg"), #testing if the image will work
         "experience": int(0),
         "description": "I'm looking for a Cat or a Dog I could take for a walk.",
         "showPets": False,
         }  ]

    for user in users:
        add_user(user["username"], user["password"], user["first_name"],
                 user["last_name"], user["last_login"], user["location"], user["dateOfBirth"],
                 user["profilePicture"], user["experience"], user["description"], user["showPets"])



    pets = [
        {"owner": User.objects.get(username="LoveIguanas"),
        "name": "Cameleon",
         "description": "I'm a wee lizard, I like to eat fruit flies and creepy spiders. I don't like grasshoppers though, YAK!",
         "species": "Lizard",
         "petPicture":models.ImageField(verbose_name="Cameleon_picture")},
        {"owner": User.objects.get(username="LoveIguanas"),
         "name": "Gecko",
         "description": "A cute, small thing!",
         "species": "Lizard",
         "petPicture": models.ImageField(verbose_name="Lizard_picture")},
        {"owner": User.objects.get(username="Doggos"),
         "name": "Anika",
         "description": "3-year old dog.",
         "species": "Dog",
         "petPicture": models.ImageField(verbose_name="Dog_picture")},
        {"owner": User.objects.get(username="anilano"),
         "name": "Monte",
         "description": "An independent cat!",
         "species": "Cat",
         "petPicture": models.ImageField(verbose_name="Cat_picture")},
        {"owner": User.objects.get(username="anilano"),
         "name": "Carno",
         "description": "Energetic and loud dog. Loves cuddling and playin with a ball.",
         "species": "Dog",
         "petPicture": models.ImageField(verbose_name="Carno_picture")} ]

    for pet in pets:
        add_pet(pet["owner"], pet["name"], pet["description"], pet["species"], pet["petPicture"])



    ratings = [
        {"madeBy": User.objects.get(username="LoveIguanas"),
         "toWho": User.objects.get(username="Doggos"),
         "rating": 3},
        {"madeBy": User.objects.get(username="Doggos"),
         "toWho": User.objects.get(username="LoveIguanas"),
         "rating": 5},
        {"madeBy": User.objects.get(username="LoveIguanas"),
         "toWho": User.objects.get(username="anilano"),
         "rating": 1},
        {"madeBy": User.objects.get(username="Doggos"),
         "toWho": User.objects.get(username="anilano"),
         "rating": 2}   ]

    for rating in ratings:
        add_rating(rating["madeBy"], rating["toWho"], rating["rating"])



    messages = [
        {"petId":Pet.objects.get(name="Cameleon"),
         "seekerUsername":UserProfile.objects.get("Doggos"),
         "date":models.DateField(auto_now_add=True),
         "messages":"Can I steal your lizard for the weekend, please?"},
        {"petId": Pet.objects.get(name="Monte"),
         "seekerUsername": UserProfile.objects.get("Doggos"),
         "date": models.DateField(auto_now_add=True),
         "messages": "That's a nice cat! Can I cuddle it?"},
        {"petId": Pet.objects.get(name="Carno"),
         "seekerUsername": UserProfile.objects.get("anilano"),
         "date": models.DateField(auto_now_add=True),
         "messages": "I love dogs! What would you say for a walk together?"},   ]

    for message in messages:
        add_message(message["petId"], message["seekerUsername"], message["date"], message["messages"])


    print(User.objects.get(username="LoveIguanas"))#testing this one!!!!!!!!!!!!!!!!!!!!!!

def add_user(username, password, first_name, last_name,
             last_login, location, dateOfBirth, profilePicture,
             experience, description, showPets):
    u = User.objects.get_or_create(username = username)[0]
    u.set_password(password)
    u.first_name = first_name
    u.last_name = last_name
    u.last_login = last_login
    u = UserProfile.objects.get_or_create(user = u)[0]
    u.location = location
    u.dateOfBirth = dateOfBirth
    u.profilePicture = profilePicture
    u.experience = experience
    u.description = description
    u.showPets = showPets
    u.save()
    return u

def add_pet(owner, name, description, species, petPicture):
    p = Pet.objects.get_or_create(owner = owner, name = name)[0]
    p.description = description
    p.species = species
    p.petPicture = petPicture
    return p


def add_rating(madeBy, toWho, rating):
    r = Rating.objects.get_or_create(madeBy = madeBy, toWho = toWho)[0]
    r.rating = rating
    return r

def add_message(petId, seekerUsername, date, messages):
    m = Messages.objects.get_or_create(petId = petId, seekerUsername = seekerUsername)[0]
    m.date = date
    m.messages = messages
    return m


# Start execution here!
if __name__ == '__main__':
    print("Starting Pawpal population script...")
    populate()
