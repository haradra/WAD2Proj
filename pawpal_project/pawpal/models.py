# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import datetime
from django.utils.timezone import *
from pawpal_project import settings

# Create your models here.

# Model for the Pet type user
# Related to base User model via one to one field constraint
class Pet(models.Model):
    SPECIES_CHOICES = (
        ('DOG', 'Dog'),
        ('CAT', 'Cat'),
        ('LIZARD', 'Lizard'),
        ('REPTILE', 'Reptile'),
        ('BIRD', 'Bird'),
        ('HAMSTER', 'Hamster')
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=False)
    description = models.CharField(max_length=300)
    species = models.CharField(max_length=10, choices=SPECIES_CHOICES)
    location = models.CharField(max_length=128)
    latitude = models.FloatField(default=55.8642)
    longitude = models.FloatField(default=4.2518)
    profilePicture = models.ImageField(upload_to='pet_images', blank=False, default='pet_images/wednesday.png')
    
    
    def save(self, *args, **kwargs):
        super(Pet, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.user.username


class Rating(models.Model):
    madeBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='madBy')
    toWho = models.ForeignKey(User, on_delete=models.CASCADE, related_name='toWho')
    rating = models.CharField(max_length=30)


    def save(self, *args, **kwargs):
        super(Rating, self).save(*args, **kwargs)

    def __str__(self):
        return "By " + str(self.madeBy) + " to " + str(self.toWho) + ":  " + str(self.rating)


# Model for the Seeker type user
# Related to base User model via one to one field constraint
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=128)
    dateOfBirth = models.DateField(default=now)
    profilePicture = models.ImageField(upload_to='profile_images', blank=False, default="profile_images/user.jpeg")
    experience = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=300)
    latitude = models.FloatField(default=55.8642)
    longitude = models.FloatField(default=4.2518)


    def save(self, *args, **kwargs):
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username



class Messages(models.Model):
    petId = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='petId')
    seekerUsername = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seekerUsername')
    date = models.DateField(default=now)
    messages = models.CharField(max_length=200)

    
    def save(self, *args, **kwargs):
        super(Messages, self).save(*args, **kwargs)

    def __str__(self):
        return self.messages
