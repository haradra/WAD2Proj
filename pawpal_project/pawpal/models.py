# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.


class Pet(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)
    species = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        super(Pet, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Rating(models.Model):
    petId = models.CharField(max_length=30)
    seekerUsername  = models.CharField(max_length=30)
    date  = models.DateField()
    messages  = models.CharField(max_length=200)

    #def save(self, *args, **kwargs):
        #super(Rating, self).save(*args, **kwargs)

    def __str__(self):
        return self.petId


class UserProfile(models.Model):
    location = models.CharField(max_length=128)
    dateOfBirth = models.DateField()
    profilePicture = models.ImageField(upload_to='profile_images', blank=True)
    experience = models.IntegerField()
    Description = models.CharField(max_length=200)
    showPets = models.BooleanField()

    user = models.OneToOneField(User) #is this line ok?
    website = models.URLField(blank=True)  #should we include this line too?

    def __str__(self):
        return self.user.username



class Messages(models.Model):
    petId = models.CharField(max_length=30)
    seekerUsername = models.CharField(max_length=30)
    date = models.DateField()
    url = models.URLField()

    def __str__(self):
        return self.user.username
