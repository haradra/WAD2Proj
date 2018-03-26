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
```python manage.py runserver```


## To enable messaging functionality

    make migrations for chat server:
      ```python manage.py migrate django_private_chat```

    run message server:
      ```python manage.py run_chat_server```

    You can talk to two different users (or to yourself) on the same machine by accessing:
        http://127.0.0.1:8000/pawpal/dialogs/user_name1
        http://localhost:8000/pawpal/dialogs/user_name2

## Running the tests

Run the test functionality by using command:

```python manage.py test```


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

See list of [contributors](https://github.com/haradra/WAD2Proj/graphs/contributors) who participated in this project.
