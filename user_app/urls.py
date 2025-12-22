from django.urls import path

from . import views

app_name="user_app"
urlpatterns=[
    path('register/', views.register_user, name='register'),
    path('home/', views.home, name='home'),
    path('my_account/', views.profile_user, name='my_account'),
    path('login/', views.login_user, name='login'),
    path('edit/<str:pk>', views.edit_profile, name='editProfile'),
    path('logout', views.log_out, name='logout'),
]