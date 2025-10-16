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
         task=form.save(commit=False)
         task.user=request.user
         task.save()
         return render(request,"task_app/create_task.html",context={"form":empty_form})

    print(empty_form)
    return render(request,"task_app/create_task.html",context={"form":empty_form})