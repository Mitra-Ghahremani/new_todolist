from django.db import models

from django.contrib.auth.models import User




class TODOLIST(models.Model):
  
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
    

class Task(models.Model):
<<<<<<< HEAD
    description = models.TextField(max_length=150)
    created_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
=======
    description=models.TextField(max_length=150)
    created_date=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=False)
    todolist=models.ForeignKey(TODOLIST,on_delete=models.CASCADE,blank=True)
>>>>>>> 4fb3f105ac882c8eb8debcaf5c7d7596e6057772
    def __str__(self):
        return self.todolist.user.username
    
    
<<<<<<< HEAD
class ToDoList(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
=======
>>>>>>> 4fb3f105ac882c8eb8debcaf5c7d7596e6057772


