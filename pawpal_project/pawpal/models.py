# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import datetime
from django.utils.timezone import *

# Create your models here.


class Pet(models.Model):
    pet = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)
    species = models.CharField(max_length=30)
    #Temporary default value for location
    location = models.CharField(max_length=30, default="Glasgow")
    petPicture = models.ImageField(upload_to='pet_images', blank=True)
    #slug = models.SlugField(unique=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Pets'
    def save(self, *args, **kwargs):
        #self.slug = slugify(self.name)
        super(Pet, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Rating(models.Model):
    FIVE_REVIEWS = (('5','5'),('4','4'),('3','3'),('2','2'),('1','1'))
    pet = models.ForeignKey(Pet, default=1)
    user = models.ForeignKey(User, default=1)
    #madeBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='madBy')
    #toWho = models.ForeignKey(User, on_delete=models.CASCADE, related_name='toWho')
    friendliness = models.PositiveIntegerField(choices=FIVE_REVIEWS, default="5")
    good_w_pets = models.PositiveIntegerField(choices=FIVE_REVIEWS, default="5")
    trust = models.PositiveIntegerField(choices= FIVE_REVIEWS, default= "5")
    class Meta:
        verbose_name_plural = 'Ratings'
        
    def save(self, *args, **kwargs):
        super(Rating, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.user)


class UserProfile(models.Model):
    #pet = models.ForeignKey(Pet, default=1)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=128)
    dateOfBirth = models.DateField(default=now)
    profilePicture = models.ImageField(upload_to='profile_images', blank=True)
    experience = models.IntegerField(default=0)
    description = models.CharField(max_length=200)
    showPets = models.BooleanField(default=False)
    #slug = models.SlugField(unique=True, blank=True)
    

    #website = models.URLField(blank=True)  #should we include this line too?

    class Meta:
        verbose_name_plural = 'Users'
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
