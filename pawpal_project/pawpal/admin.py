# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from pawpal.models import UserProfile, Pet, Rating, Messages


# Defined fields for models
class PetAdmin(admin.ModelAdmin):
    list_display = ('user','name','description')

class RatingAdmin(admin.ModelAdmin):
    list_display = ('toWho', 'madeBy', 'rating')
    

class MessagesAdmin(admin.ModelAdmin):
    list_display = ('petId', 'seekerUsername', 'date')

    

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", 'location', "dateOfBirth", 'experience', 'description')



#Registering models
admin.site.register(Pet, PetAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Messages, MessagesAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
