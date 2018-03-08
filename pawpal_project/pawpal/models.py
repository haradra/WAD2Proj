# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.


class Pet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)
    species = models.CharField(max_length=30)
    petPicture = models.ImageField(upload_to='pet_images', blank=True)

    #def save(self, *args, **kwargs):
        #super(Pet, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Rating(models.Model):
    madeBy = models.ForeignKey(User, on_delete=models.CASCADE)
    toWho = models.ForeignKey(Pet, on_delete=models.CASCADE)
    rating = models.CharField(max_length=30)

    #def save(self, *args, **kwargs):
        #super(Rating, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.toWho) + ":  " + str(self.rating)


class UserProfile(models.Model):
    username = models.CharField(max_length=30, unique = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=128)
    dateOfBirth = models.DateField(auto_now_add=True)
    profilePicture = models.ImageField(upload_to='profile_images', blank=True)
    experience = models.IntegerField(default=0)
    description = models.CharField(max_length=200)
    showPets = models.BooleanField(default=False)

    #website = models.URLField(blank=True)  #should we include this line too?

    #def save(self, *args, **kwargs):
        #super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username



class Messages(models.Model):
    petId = models.ForeignKey(Pet, on_delete=models.CASCADE)
    seekerUsername = models.ForeignKey(User)
    date = models.DateField(auto_now_add=True)
    messages = models.CharField(max_length=200)

    #def save(self, *args, **kwargs):
        #super(Messages, self).save(*args, **kwargs)

    def __str__(self):
        return self.messages
