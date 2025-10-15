from django.urls import path
from . import views

app_name="user_app"

urlpatterns=[
    path('register/',views.registerUser,name='register'),
    path('home/',views.home,name='home'),
    path('my_account/',views.profileUser,name='my_account'),
    path('login/',views.loginUser,name='login'),
    path('edit/<str:pk>',views.editProfile,name='editProfile')
]