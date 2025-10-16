from django.db import models
from user_app.models import userProfile
class Task(models.Model):

    userProfile=models.ForeignKey(userProfile,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=300)
    created=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}"