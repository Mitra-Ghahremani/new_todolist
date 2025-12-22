from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .forms import UserProfileForm,UserForm,LoginForm,UserEditForm
from .models import UserProfile



def home(request):
    context = {}
    return render(request,"user_app/home.html",context)


def register_user(request):
    user = UserForm()
    profile = UserProfileForm()
    if request.method == "POST":
        user = UserForm(request.POST)
        profile = UserProfileForm(request.POST)
        if user.is_valid() and profile.is_valid():
            user = user.save(commit=False)
            user.set_password(user.password)
            user.save()
            profile = profile.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('user_app:home')
        

        return render(request, 'user_app/register.html', context={'user':user, 'profile':profile})
  

    return render(request, "user_app/register.html", context={'user':user, 'profile':profile})



def login_user(request):
    form = LoginForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('user_app:my_account')
        

        return render(request, 'user_app/login.html', context={'form':form})
    

    return render(request, 'user_app/login.html', context={'form':form})


@login_required
def profile_user(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'user_app/profile.html', context={'profile':profile})


@login_required   
def edit_profile(request, pk):
    profile_object = get_object_or_404(UserProfile, id=pk)
    profile = UserProfileForm(instance=profile_object)
    user=UserEditForm(instance=request.user) 
    if request.method == 'POST':
        user = UserEditForm(request.POST , instance=request.user)
        profile = UserProfileForm(request.POST, instance=profile_object)
        if user.is_valid() and profile.is_valid():
            user.save()
            profile.save()
            return redirect('user_app:my_account')
        

    return render(request, "user_app/editprofile.html", context={"user":user, "profile":profile})
 
      
def log_out(request):
         logout(request)
         return redirect("user_app:login")
         
  
