from django.shortcuts import render
from .models import Task
from .forms import createTaskForm
from django.contrib.auth.decorators import login_required

@login_required
def createTask(request):
    
    empty_form=createTaskForm()
    if request.method=='POST':
      form=createTaskForm(request.POST)
      if form.is_valid():
         object=form.save(commit=False)
         #در ارتباط بیتن پروفایل و تسک به مشکل برخوردم فک میکنم باید برم بین تسک و یوزر ارتباط ایجاد کنم
         object.save()
         return render(request,"task_app/create_task.html",context={"form":empty_form})

    print(empty_form)
    return render(request,"task_app/create_task.html",context={"form":empty_form})