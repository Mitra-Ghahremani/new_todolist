from django.urls import path
from . import views

app_name="task_app"

urlpatterns=[path("create_task/",views.createTask,name='create_task'),]
