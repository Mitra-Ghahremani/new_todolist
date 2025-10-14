from django.db import models
from user_app.models import userProfile
class Task(models.Model):
    profile=models.ForeignKey(userProfile,on_delete=models.CASCADE)
    name=models.CharField(max_length=300)
    created=models.DateField(auto_now_add=True)