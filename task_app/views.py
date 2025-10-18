from django.shortcuts import render,redirect
from .models import Task
from .forms import createTaskForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

@login_required
def createTask(request):
    empty_form=createTaskForm()
    if request.method=='POST':
      form=createTaskForm(request.POST)
      if form.is_valid():
         task=form.save(commit=False)
         task.user=request.user
         print(task.user)
         task.save()
         return render(request,"task_app/create_task.html",
                       context={"form":empty_form,"message":"تسک شما با موفقیت اضافه شد"})
   
    return render(request,"task_app/create_task.html",context={"form":empty_form})

@login_required
def displayTask(request):
   tasks=Task.objects.filter(user_id=request.user.id)
   print(tasks)
   if tasks:
         return render(request,"task_app/display_task.html",context={'tasks':tasks})
   return HttpResponse ("هیچ تسکی برای این کاربر وجود ندارد")


@login_required   
def editTask(request,id):
    task=get_object_or_404(Task,id=id)
    if request.method=="POST":
        form=createTaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_app:display_task')
        return render(request,"task_app/edit_task.html",context={"form":form})
    form=createTaskForm(instance=task)
    return render(request,"task_app/edit_task.html",context={'form':form})




      
