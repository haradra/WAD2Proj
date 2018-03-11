# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from pawpal.models import UserProfile, Pet, Rating, Messages


class PetAdmin(admin.ModelAdmin):
    list_display = ('name', "owner",'description')
    #prepopulated_fields = {'slug':('name',)}
class RatingAdmin(admin.ModelAdmin):
    list_display = ('toWho', 'madeBy', 'rating')
    #prepopulated_fields = {'slug': ('toWho',)}
    

class MessagesAdmin(admin.ModelAdmin):
    list_display = ('petId', 'seekerUsername', 'date')
    #prepopulated_fields = {'slug': ('seekerUsername',)}
    

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", 'location', "dateOfBirth", 'experience', 'description')
    #prepopulated_fields = {'slug': ('user',)}

# Register your models here.

admin.site.register(Pet, PetAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Messages, MessagesAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
