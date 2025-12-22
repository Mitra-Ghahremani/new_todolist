from django.contrib.auth.models import User
from django import forms

from .models import UserProfile



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password"] 


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']  


class UserEditForm(forms.ModelForm):
     class Meta:
        model = User
        fields = ["first_name", "last_name", "email"] 
         