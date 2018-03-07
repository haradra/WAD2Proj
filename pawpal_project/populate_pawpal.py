import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'pawpal_project.settings')

import pawpal
from django.db import models
pawpal.setup()
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




"""

    python_pages = [
        {"title": "Official Python Tutorial",
         "url":"http://docs.python.org/2/tutorial/",
         "views": 1},
        {"title":"How to Think like a Computer Scientist",
         "url":"http://www.greenteapress.com/thinkpython/",
         "views": 4},
        {"title":"Learn Python in 10 Minutes",
         "url":"http://www.korokithakis.net/tutorials/python/",
         "views": 9} ]

    django_pages = [
        {"title":"Official Django Tutorial",
         "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/",
         "views": 123},
        {"title":"Django Rocks",
         "url":"http://www.djangorocks.com/",
         "views": 14},
        {"title":"How to Tango with Django",
         "url":"http://www.tangowithdjango.com/",
         "views": 11} ]

    other_pages = [
        {"title":"Bottle",
         "url":"http://bottlepy.org/docs/dev/",
         "views": 1},
        {"title":"Flask",
         "url":"http://flask.pocoo.org",
         "views": 6} ]

    cats = {"Python": {"pages": python_pages, "views": 128, "likes": 64},
            "Django": {"pages": django_pages, "views": 64, "likes": 32},
            "Other Frameworks": {"pages": other_pages, "views": 32, "likes": 16} }

    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.
    # if you are using Python 2.x then use cats.iteritems() see
    # http://docs.quantifiedcode.com/python-anti-patterns/readability/
    # for more information about how to iterate over a dictionary properly.

    for cat, cat_data in cats.items():
        c= add_cat(cat, cat_data["views"], cat_data["likes"])
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"], p["views"])

    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.likes=likes
    c.views=views
    c.save()
    return c
"""


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
