from django import forms
from django.contrib.auth.models import User
from pawpal.models import UserProfile, Pet, Rating, Messages
import datetime



class PetForm(forms.ModelForm):
    """
    name = forms.CharField(max_length=50, help_text="Please enter your pet's name.")
    """
    location = forms.CharField(max_length=50, help_text="Please enter your location.")
    latitude = forms.FloatField(widget=forms.HiddenInput(), initial=55.8642)
    longitude = forms.FloatField(widget=forms.HiddenInput(), initial=4.2518)
    class Meta:
        model = Pet
        exclude = ('first_name', 'last_name')
        fields = ('location', 'name', 'species', 'description', 'profilePicture','latitude', 'longitude')

      
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(widget=forms.EmailInput())
    
    class Meta:
        
        model = User
        fields = ('username', 'password', "first_name", "last_name", "email", "is_active")


class UserProfileForm(forms.ModelForm):
    
    location = forms.CharField(max_length=128, required=True)
    """
    dateOfBirth = forms.DateField(initial=datetime.date.today)
    profilePicture = forms.ImageField(required=False)
    experience = forms.IntegerField(initial=0)
    showPets = forms.BooleanField(initial=False)
    """
    latitude = forms.FloatField(widget=forms.HiddenInput(), initial=55.8642)
    longitude = forms.FloatField(widget=forms.HiddenInput(), initial=4.2518)

    class Meta:
        model = UserProfile
        fields = ('location', 'dateOfBirth','profilePicture', 'description','experience','latitude','longitude')

class UpdatePetProfile(forms.ModelForm):
    
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    

    class Meta:
        model = Pet
        fields = ('username', "first_name", "last_name", "email",'species', 'description', 'profilePicture')

    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        return email
class UpdateUserProfile(forms.ModelForm):
    
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    dateOfBirth = forms.DateField(required=False)

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'first_name', 'last_name', 'experience', 'profilePicture', 'dateOfBirth')

    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        return email

