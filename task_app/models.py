from django.db import models
from django.contrib.auth.models import User




class TODOLIST(models.Model):
  
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
    

class Task(models.Model):
    description=models.TextField(max_length=150)
    created_date=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=False)
    todolist=models.ForeignKey(TODOLIST,on_delete=models.CASCADE,blank=True)
    def __str__(self):
        return self.description
    
    


