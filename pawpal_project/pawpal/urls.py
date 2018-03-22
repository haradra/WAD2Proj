"""pawpal_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from pawpal import views
from django_private_chat import urls as django_private_chat_urls

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^password/$', views.password, name='password'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^register/$', views.register, name='register'),
    url(r'^editaccount/$', views.editaccount, name='editaccount'),
    url(r'^profile/(?P<username>[a-zA-Z0-9]+)/$', views.get_user_profile, name='user_profile'),
    url(r'^myaccount/$', views.myaccount, name='myaccount'),
    url(r'^rating/$', views.create_rating, name='rating'),
    url(r'^', include('django_private_chat.urls')),
]
