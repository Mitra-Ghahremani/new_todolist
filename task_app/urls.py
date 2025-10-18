from django.urls import path
from . import views

app_name="task_app"

urlpatterns=[path("create_task/",views.createTask,name='create_task'),
             path("display_task/",views.displayTask,name="display_task"),
             path("edit_task/<int:id>/",views.editTask,name="edit_task"),]
