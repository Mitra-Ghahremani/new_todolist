from django.urls import path

from . import views

app_name="task_app"
urlpatterns=[path("create_task/", views.create_task, name='create_task'),
             path("display_task/", views.display_task, name="display_task"),
             path("edit_task/<int:id>/", views.edit_task, name="edit_task"),
             path("delete_task/<int:id>", views.delete_task, name="delete_task"),
             path("end_task/<int:id>", views.end_task, name="end_task")]
