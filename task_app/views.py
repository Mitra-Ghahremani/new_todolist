from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Task, ToDoList
from .forms import CreateTaskForm




@login_required
def create_task(request):
    empty_form = CreateTaskForm()
    if request.method == 'POST':
      form=CreateTaskForm(request.POST)
      if form.is_valid():
         form=form.save(commit=False)
         form.todolist_id=request.user.id
         form.save()
         return render(request,
                       "task_app/create_task.html",
                       context={"form":empty_form, "message":"تسک شما با موفقیت اضافه شد"}
                               )
      

    return render(request,"task_app/create_task.html",context={"form":empty_form})


def display_task(request):
   task=Task.objects.filter(todolist_id=request.user.id)
   print(task)
   if task:
       return render(request,"task_app/display_task.html",context={"task":task})
   return  HttpResponse ("برای این کاربر تسکی وجود ندارد")


@login_required   
def edit_task(request, id):
    task = Task.objects.get(id=id) 
    form=CreateTaskForm(instance=task)
    if request.method == "POST":
        form = CreateTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_app:display_task')
        

        return render(request, 
                     "task_app/edit_task.html",
                      context={"message":"تسک  باید حداکثر 150 کاراکتر داشته باشد"})
    

    return render(request, 
                  "task_app/edit_task.html", 
                   context={'form':form})


@login_required
def delete_task(request, id):
    task = Task.objects.get(id=id)
    if request.method == "POST":
        task.delete()
        return HttpResponse("تسک شما با موفقیت حذف گردید")
    

    return render(request,
                  "task_app/delete_task.html", 
                  context={'task':task})


@login_required
def end_task(request, id):
    task = Task.objects.get(id=id)
    task.status = True 
    task.save()
    return redirect("task_app:display_task")

