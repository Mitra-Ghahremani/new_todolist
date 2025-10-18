from django.db import models
from django.contrib.auth.models import User



class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    task_name=models.CharField(max_length=50)
    created=models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.task_name}"