from django import forms
from .models import userProfile
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password","password"] 

class userProfileForm(forms.ModelForm):
    class Meta:
        model=userProfile
        exclude=['user']