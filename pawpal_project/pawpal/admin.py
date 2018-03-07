# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from pawpal.models import UserProfile, Pet, Rating, Messages

"""
class PetAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'description')

class RatingAdmin(admin.ModelAdmin):
    #prepopulated_fields = {'slug': ('name',)}

class MessagesAdmin(admin.ModelAdmin):
    #prepopulated_fields = {'slug': ('name',)}
"""

# Register your models here.

admin.site.register(Pet)#, PetAdmin)
admin.site.register(Rating)#, RatingAdmin)
admin.site.register(Messages)#, MessagesAdmin)
admin.site.register(UserProfile)
