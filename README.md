# PawPal - Web Application Development Project

This is a group project undertaken under the WAD2 module. The purpose of this web-app is to connect animal lovers in general, especially people unable to have pets that want to spend time with animals, with people who do not have time to take satisfactory care of their pets.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Prerequisites

Please clone this repository to a local system, set up a virtual environment and install the required libraries listed in our [REQUIREMENTS](https://github.com/haradra/WAD2Proj/blob/master/requirements.txt). Note: Python version 3.0+ is required for the virtual environment.

Example:

```mkvirtualenv --python=/usr/bin/python3 python3```

```pip install -r requirements.txt```

## Running the application locally

Change to the pawpal_project directory and run:

```python manage.py runserver``` (Use localhost instead of the loopback address)

NOTE: In order the social media connection to work use localhost rather than 127.0.0.1
The keys for the social media are sent by email. You must place these keys into pawpal_project/pawpal_project directory.
Read the section ##Additional information below ## Running the tests section.

## To enable messaging functionality

    make migrations for chat server:
      python manage.py migrate django_private_chat

    run message server:
      python manage.py run_chat_server

    You can talk to two different users (or to yourself) on the same machine by accessing:
        http://127.0.0.1:8000/pawpal/dialogs/user_name1
        http://localhost:8000/pawpal/dialogs/user_name2

## Running the tests

Run the test functionality by using command:

```python manage.py test```


##Additional information (Please, read!)

*We know that this way of dealing with the keys for the social media is not the best because it is coupled our code to
*sensative data. However, becasue of time constraints, we were not be able to effectively decouple them.
*This is how we would have done it:

 1) Create a file called pawpal_project/keys.py
 2) Paste in the keys to that file
 3) Add pawpal_project/keys.py to our .gitignore file

 (We did the first three steps)

 4) In settings.py add these lines of code:

 with open('keys.py', 'r') as f:
 SOCIAL_MEDIA_KEYS = f.read().strip()

 5) In views.py add:

 from django.conf import settings

 6) To access the the keys you need to do:

 key = settings.SOCIAL_MEDIA_KEYS

 *We did originally have the keys in the repository, as they show in the commit history. However, we learnt as we went along
 *that is not a good thing to do.

## WhiteNoise
 ***We tried to implement WhiteNoise in our project so Django to be able to recognise static files even when the DEBUG was
 set to False, but we did not manage to complete that on time before the deadline.


## Deployment

This web application is deployed on [PythonAnywhere](https://www.pythonanywhere.com).

Link:

[PawPal](https://pawpal.pythonanywhere.com/)


## Built With

* [Google Maps JavaScript API](https://developers.google.com/maps/documentation/javascript/)
* [jQuery](https://jquery.com/)
* [Bootstrap 3](https://getbootstrap.com/docs/3.3/)


## External Sources

* Tango With Django: A beginner's Guide to Web Development With Django 1.9 (Leif Azzopardi, David Maxwell)
* Picture sources: www.pexels.com
* Private Chat functionality: https://github.com/Bearle/django-private-chat


## Team Members

*Adam Czyzewski
*Ivelina Doynova
*Malgorzata Kurkiewicz
*Milosz Krawiec

See list of [contributors](https://github.com/haradra/WAD2Proj/graphs/contributors) who participated in this project.


## Areas of future improvement/development:
    - more animal categories,
    - leaving reviews of pets/users,
    - blocking users,
    - 'Favourites' category,
    - location range - e.g. all pets within 50 km
    - "booking animal" - adding a feature that would enable booking slots when the user could do some activity with a pet
    - adding calendar option (as above)
    - adding "Report to admin"
    - captcha for registration
    - Adding adds on the website
    - enabling deleting the account
    - ADDING TERMS AND CONDITIONS

       