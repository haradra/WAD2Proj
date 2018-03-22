# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import datetime
from django.utils.timezone import *
from pawpal_project import settings

# Create your models here.


class Pet(models.Model):
    SPECIES_CHOICES = (
        ('DOG', 'Dog'),
        ('CAT', 'Cat'),
        ('LIZARD', 'Lizard'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=False)
    description = models.CharField(max_length=200)
    species = models.CharField(max_length=10, choices=SPECIES_CHOICES)
    #Temporary default value for location
    location = models.CharField(max_length=50)
    latitude = models.FloatField(default=55.8642)
    longitude = models.FloatField(default=4.2518)
    profilePicture = models.ImageField(upload_to='pet_images', blank=True)
    #slug = models.SlugField(unique=True, blank=True)
    
    
    def save(self, *args, **kwargs):
        #self.slug = slugify(self.name)
        super(Pet, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.user.username


class Rating(models.Model):
    madeBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='madBy')
    toWho = models.ForeignKey(User, on_delete=models.CASCADE, related_name='toWho')
    rating = models.CharField(max_length=30)
    #slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        #Same question, what are we slugifying, is slug even necessary here?
        #Need to think how will the URL look
        #self.slug = slugify(self.)
        super(Rating, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.toWho) + ":  " + str(self.rating)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=128)
    dateOfBirth = models.DateField(default=now)
    profilePicture = models.ImageField(upload_to='profile_images', blank=True, default="profile_images/user.jpeg")
    experience = models.IntegerField(default=0)
    description = models.CharField(max_length=200)
    latitude = models.FloatField(default=55.8642)
    longitude = models.FloatField(default=4.2518)
    #slug = models.SlugField(unique=True, blank=True)

    #website = models.URLField(blank=True)  #should we include this line too?

    def save(self, *args, **kwargs):
        #What are we slugifying to here? user for now
        #self.slug = slugify(self.user)
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username



class Messages(models.Model):
    petId = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='petId')
    seekerUsername = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seekerUsername')
    date = models.DateField(default=now)
    messages = models.CharField(max_length=200)
    #slug = models.SlugField(unique=True)
    def save(self, *args, **kwargs):
        
        #self.slug = slugify(self.)
        super(Messages, self).save(*args, **kwargs)

    def __str__(self):
        return self.messages
