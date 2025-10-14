from django.db import models
from django.contrib.auth.models import User


class userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    bio=models.TextField(max_length=1000,blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    phone_number=models.CharField(max_length=11,null=True,blank=True)
    address=models.CharField(max_length=500,blank=True,null=True)
    created=models.DateField(auto_now_add=True)
    image=models.ImageField(blank=True,null=True,upload_to="user_app/images/",default="user_app/images/default.jpg")