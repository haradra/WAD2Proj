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
         "location": "Glasgow",
         "latitude": float(25.0),
         "longitude": float(25.0),
         "dateOfBirth": datetime.date(1995, 2, 1),
         "profilePicture": "profile_images/1.jpeg",
         "experience": int(4),
         "is_active":True,
         "description": "I love Iguanas, like really. Iguanas <3",
         "email": "sample_email@sample.com",
         },
        {"username": "Doggos",
         "password": "IreallyLoveDoggos123456789",
         "first_name": "Anna",
         "last_name": "Nicole",
         "location": "Glasgow",
         "latitude": float(25.0),
         "longitude": float(25.0),
         "dateOfBirth": datetime.date(1995, 2, 1),
         "profilePicture": "profile_images/2.jpeg",
         "experience": int(8),
         "is_active":True,
         "description": "Doggos, doggos, I have one, let's spend with him all our time!",
         "email": "sample_ema2il@sample.com",
         },
        {"username": "anilano",
         "password": "Irsdawnilano123456789",
         "first_name": "Anilano",
         "last_name": "Korton",
         "location": "Edinburgh",
         "latitude": float(25.0),
         "longitude": float(25.0),
         "dateOfBirth": datetime.date(1995, 2, 1),
         "profilePicture": "profile_images/3.jpeg",
         "experience": int(0),
         "is_active":False,
         "description": "I'm looking for a Cat or a Dog I could take for a walk.",
         "email": "3sample_email@sample.com",
         }  ]

    for user in users:
        add_user(user)

    pets = [
        {"username": "cameleon123",
         "password":"qwerty12345",
        "name": "Cameleon",
         "description": "I'm a wee lizard, I like to eat fruit flies and creepy spiders. I don't like grasshoppers though, YAK!",
         "species": "Lizard",
         "location": "Glasgow",
         "latitude": float(25.0),
         "longitude": float(25.0),
         "is_active":True,
         "profilePicture": "pet_images/1.jpeg",
         "email": "sample_email32132@sample.com"},
        {"username": "doggo123",
         "password":"qwerty12345",
         "name": "Gecko",
         "description": "A cute, small thing!",
         "species": "Lizard",
         "location": "Edinburgh",
         "latitude": float(25.0),
         "longitude": float(25.0),
         "is_active":True,
         "profilePicture": "pet_images/2.jpeg",
         "email": "sssss32132@sample.com"},
        {"username": "birdo123",
         "password":"qwerty12345",
         "name": "Anika",
         "description": "3-year old dog.",
         "species": "Dog",
         "location": "London",
         "latitude": float(25.0),
         "longitude": float(25.0),
         "is_active":True,
         "profilePicture": "pet_images/3.jpeg",
         "email": "ilikecake@sample.com"},
        {"username": "catto123",
         "password":"qwerty12345",
         "name": "Monte",
         "description": "An independent cat!",
         "species": "Cat",
         "location": "Glasgow",
         "latitude": float(25.0),
         "longitude": float(25.0),
         "is_active":False,
         "profilePicture": "pet_images/4.jpeg",
         "email": "ireallylikecake@sample.com"},
        {"username": "lizardo123",
         "password":"qwerty12345",
         "name": "Carno",
         "description": "Energetic and loud dog. Loves cuddling and playin with a ball.",
         "species": "Dog",
         "location": "Glasgow",
         "latitude": float(25.0),
         "longitude": float(25.0),
         "is_active":False,
         "profilePicture": "pet_images/5.jpeg",
         "email": "cooookies@sample.com"} ]

    for pet in pets:
        add_pet(pet)

    ratings = [
        {"madeBy": User.objects.get(username="LoveIguanas"),
         "toWho": User.objects.get(username="Doggos"),
         "rating": 3},
        {"madeBy": User.objects.get(username="LoveIguanas"),
         "toWho": User.objects.get(username="catto123"),
         "rating": 3},
        {"madeBy": User.objects.get(username="LoveIguanas"),
         "toWho": User.objects.get(username="cameleon123"),
         "rating": 5},
        {"madeBy": User.objects.get(username="LoveIguanas"),
         "toWho": User.objects.get(username="lizardo123"),
         "rating": 3},
        {"madeBy": User.objects.get(username="lizardo123"),
         "toWho": User.objects.get(username="anilano"),
         "rating": 5},
        {"madeBy": User.objects.get(username="LoveIguanas"),
         "toWho": User.objects.get(username="anilano"),
         "rating": 5},
        {"madeBy": User.objects.get(username="Doggos"),
         "toWho": User.objects.get(username="cameleon123"),
         "rating": 5},
        {"madeBy": User.objects.get(username="Doggos"),
         "toWho": User.objects.get(username="anilano"),
         "rating": 2},
        {"madeBy": User.objects.get(username="lizardo123"),
         "toWho": User.objects.get(username="anilano"),
         "rating": 3},
        {"madeBy": User.objects.get(username="anilano"),
         "toWho": User.objects.get(username="birdo123"),
         "rating": 1},
        {"madeBy": User.objects.get(username="anilano"),
         "toWho": User.objects.get(username="birdo123"),
         "rating": 1},
        {"madeBy": User.objects.get(username="Doggos"),
         "toWho": User.objects.get(username="birdo123"),
         "rating": 1},
        {"madeBy": User.objects.get(username="Doggos"),
         "toWho": User.objects.get(username="birdo123"),
         "rating": 5},
        {"madeBy": User.objects.get(username="doggo123"),
         "toWho": User.objects.get(username="birdo123"),
         "rating": 5},
        {"madeBy": User.objects.get(username="anilano"),
         "toWho": User.objects.get(username="doggo123"),
         "rating": 2}   ]

    for rating in ratings:
        add_rating(rating["madeBy"], rating["toWho"], rating["rating"])


def add_user(user):
    u = User.objects.get_or_create(username = user["username"])[0]
    u.set_password(user["password"])
    u.first_name = user["first_name"]
    u.last_name = user["last_name"]
    u.email = user["email"]
    u.save()
    u = UserProfile.objects.get_or_create(user = u)[0]
    u.location = user["location"]
    u.latitude = user["latitude"]
    u.longitude = user["longitude"]
    u.dateOfBirth = user["dateOfBirth"]
    u.profilePicture = user["profilePicture"]
    u.experience = user["experience"]
    u.description = user["description"]
    u.is_active = user["is_active"]
    u.save()
    return u

def add_pet(pet):
    p = User.objects.get_or_create(username = pet["username"])[0]
    p.set_password(pet["password"])
    p.email = pet["email"]
    p.save()
    p = Pet.objects.get_or_create(user=p)[0]
    p.name = pet["name"]
    p.description = pet["description"]
    p.species = pet["species"]
    p.location = pet["location"]
    p.latitude = pet["latitude"]
    p.longitude = pet["longitude"]
    p.profilePicture = pet["profilePicture"]
    p.is_active = pet["is_active"]
    p.save()
    return p

def add_rating(madeBy, toWho, rating):
    r = Rating.objects.get_or_create(madeBy = madeBy, toWho = toWho)[0]
    r.rating = rating
    r.save()
    return r

def add_message(petId, seekerUsername, date, messages):
    m = Messages.objects.get_or_create(petId = petId, seekerUsername = seekerUsername)[0]
    m.date = date
    m.messages = messages
    m.save()
    return m


# Start execution here!
if __name__ == '__main__':
    print("Starting Pawpal population script...")
    populate()
