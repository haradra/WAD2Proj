from django import forms
from django.contrib.auth.models import User
from pawpal.models import UserProfile, Pet, Rating, Messages
import datetime


#It's only a scheleton for a forms.py file. Need to be edited, funcionalities added etc.

class PetForm(forms.ModelForm):
    name = forms.CharField(max_length=50, help_text="Please enter your pet's name.")
    location = forms.CharField(max_length=50, help_text="Please enter your location.")
    class Meta:
        model = Pet
        fields = "__all__"

      
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        
        model = User
        fields = ('username', 'password', "first_name", "last_name", "is_active")



#This form was importing model input fields, why? Changed to form, if mistake
#for some reason let me know        
class UserProfileForm(forms.ModelForm):
    location = forms.CharField(max_length=128)
    dateOfBirth = forms.DateField(initial=datetime.date.today)
    #Think this overrides the model image i.e not needed
    profilePicture = forms.ImageField(required=False)
    experience = forms.IntegerField(initial=0)
    description = forms.CharField(max_length=200, required=False)
    showPets = forms.BooleanField(initial=False)


    class Meta:
        model = UserProfile
        fields = ('location', 'dateOfBirth','profilePicture')

class UpdateProfile(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        return email

