import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'pawpal_project.settings')

import django
from django.db import models
django.setup()
from pawpal.models import Pet, Rating, Messages, UserProfile

def populate():

    users = [
        {"username":"LoveIguanas",
         "password": "IreallyLoveIguanas123456789",
         "first_name":"Donald",
         "last_name": "Duck",
         "last_login": models.DatetimeField(auto_now_add=True),
         "location": "Glasgow",
         "dateOfBirth": models.DatetimeField(auto_now_add=True),
         "profilePicture": models.ImageField(verbose_name="picture"),
         "experience": 4,
         "description": "I love Iguanas, like really. Iguanas <3",
         "showPets": False,
         "pets": loveIguanas_pets,
         }
        {"username": "Doggos",
         "password": "IreallyLoveDoggos123456789",
         "first_name": "Mark",
         "last_name": "Nicold",
         "last_login": models.DatetimeField(auto_now_add=True),
         "location": "Glasgow",
         "dateOfBirth": models.DatetimeField(auto_now_add=True),
         "profilePicture": models.ImageField(verbose_name="picture"),
         "experience": 8,
         "description": "Doggos, doggos, I have one, let's spend with him all our time!",
         "showPets": True,
         "pets": doggos_pets,
         }
        {"username": "anilano",
         "password": "Irsdawnilano123456789",
         "first_name": "Anilano",
         "last_name": "Korton",
         "last_login": models.DatetimeField(auto_now_add=True),
         "location": "Edinburgh",
         "dateOfBirth": models.DatetimeField(auto_now_add=True),
         "profilePicture": models.ImageField(verbose_name="picture"),
         "experience": 0,
         "description": "I'm looking for a Cat or a Dog I could take for a walk.",
         "showPets": False,
         "pets": anilano_pets,
         }  ]

    loveIguanas_pets =
    doggos_pets =
    anilano_pets =


    pets = [


    ]


    ratings = [


    ]


    messages = [


    ]


def add_user(username, password, first_name,
             last_name, last_login, location, dateOfBirth,
             profilePicture, experience, description, showPets):
    u = UserProfile.objects.get_or_create(username = username)[0]
    u.user.username = username
    u.user.password = password
    u.user.first_name = first_name
    u.user.last_name = last_name
    u.user.last_login = last_login
    u.location = location
    u.dateOfBirth = dateOfBirth
    u.profilePicture = profilePicture
    u.experience = experience
    u.description = description
    u.showPets = showPets
    u.save()
    return u

def add_pet():


def add_rating():


def add_message():



# Start execution here!
if __name__ == '__main__':
    print("Starting Pawpal population script...")
    populate()
