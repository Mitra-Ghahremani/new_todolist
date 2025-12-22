from django.db import models

from django.contrib.auth.models import User



class Task(models.Model):
    description = models.TextField(max_length=150)
    created_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.description
    
    
class ToDoList(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username


