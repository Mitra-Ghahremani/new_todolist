from django.shortcuts import render,redirect
from .forms import UserProfileForm,UserForm,LoginForm,userEditForm
from .models import userProfile
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from  task_app.models import TODOLIST



def home(request):
    context={}
    return render(request,"user_app/home.html",context)


def registerUser(request):
    if request.method=="POST":
        user=UserForm(request.POST)
        profile=UserProfileForm(request.POST)
        if user.is_valid() and profile.is_valid():
            user=user.save(commit=False)
            user.set_password(user.password)
            user.save()
           
            profile=profile.save(commit=False)
            profile.user=user
            profile.save()
            Todolist=TODOLIST(user=user)
            Todolist.save()
            print("profile is:",profile)
            return redirect('user_app:home')
        return render(request,'user_app/register.html',context={'user':user,'profile':profile})
    user=UserForm()
    profile=UserProfileForm()
    return render(request,"user_app/register.html",context={'user':user,'profile':profile})

def loginUser(request):
    form=LoginForm()
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('user_app:my_account')
        return render(request,'user_app/login.html',context={'form':form})
    return render(request,'user_app/login.html',context={'form':form})


@login_required
def profileUser(request):
        profile=get_object_or_404(userProfile,user=request.user)
        return render(request,'user_app/profile.html',context={'profile':profile})

@login_required   
def editProfile(request,pk):
        profileObject=get_object_or_404(userProfile,id=pk)
        profile=UserProfileForm(instance=profileObject)
        user=userEditForm(instance=request.user) 
        if request.method=='POST':
            user=userEditForm(request.POST , instance=request.user)
            profile=UserProfileForm(request.POST , instance=profileObject)
            if user.is_valid() and profile.is_valid():
                user.save()
                profile.save()
                return redirect('user_app:my_account')
            return render(request,"user_app/editprofile.html",context={"user":user,"profile":profile})

        return render(request,"user_app/editprofile.html",
                      context={'user':user,'profile':profile})


def Logout(request):
         logout(request)
         return redirect("user_app:login")
         
  
