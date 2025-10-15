from django import forms
from .models import userProfile
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password"] 



class UserProfileForm(forms.ModelForm):
    class Meta:
        model=userProfile
        exclude=['user']

class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']  

class userEditForm(forms.ModelForm):
     class Meta:
        model=User
        fields=["first_name","last_name","email"] 
         