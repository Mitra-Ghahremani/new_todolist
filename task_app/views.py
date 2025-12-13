from django.shortcuts import render,redirect
from .models import Task,TODOLIST
from .forms import createTaskForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def createTask(request):
    empty_form=createTaskForm()
    if request.method=='POST':
      form=createTaskForm(request.POST)
      if form.is_valid():
         task=form.save()
         todolist=TODOLIST(task=task,user=request.user)
         todolist.save()
         return render(request,"task_app/create_task.html",
                       context={"form":empty_form,"message":"تسک شما با موفقیت اضافه شد"})
    return render(request,"task_app/create_task.html",context={"form":empty_form})


@login_required
def displayTask(request):
   todolist=TODOLIST.objects.filter(user=request.user)
   print(todolist)
   if todolist:
         return render(request,"task_app/display_task.html",context={'todolist':todolist})
   return HttpResponse (" تو دو لیست برای این کاربر وجود ندارد")


@login_required   
def editTask(request,id):
    task=Task.objects.get(id=id)
    if request.method=="POST":
        form=createTaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_app:display_task')
        return render(request,"task_app/edit_task.html",context={"message":"تسک  باید حداکثر 150 کاراکتر داشته باشد"})
    form=createTaskForm(instance=task)
 
    return render(request,"task_app/edit_task.html",context={'form':form})


@login_required
def deleteTask(request,id):
    task=Task.objects.get(id=id)
    print(task)
    if request.method == "POST":
        task.delete()
        return HttpResponse("تسک شما با موفقیت حذف گردید")
    return render(request,"task_app/delete_task.html",context={'task':task})

      
