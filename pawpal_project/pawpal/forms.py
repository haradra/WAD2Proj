from django import forms
from django.contrib.auth.models import User
from pawpal.models import UserProfile, Pet, Rating, Messages


#It's only a scheleton for a forms.py file. Need to be edited, funcionalities added etc.

class PetForm(forms.ModelForm):
    name = forms.CharField(max_length=50, help_text="Please enter your pet's name.")

    class Meta:
        model = Pet




class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', "first_name", "last_name")




class UserProfileForm(forms.ModelForm):
    location = models.CharField(max_length=128)
    dateOfBirth = models.DateField(default=now)
    profilePicture = models.ImageField(upload_to='profile_images', blank=True)
    experience = models.IntegerField(default=0)
    description = models.CharField(max_length=200)
    showPets = models.BooleanField(default=False)


    class Meta:
        model = UserProfile
        fields = ('website', 'picture')