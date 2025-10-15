from django.shortcuts import render,redirect
from .forms import UserProfileForm,UserForm,LoginForm
from .models import userProfile
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

def home(request):
    context={}
    return render(request,"user_app/home.html",context)


def registerUser(request):
    if request.method=="POST":
        user=UserForm(request.POST)
        profile=UserProfileForm(request.POST)

        if user.is_valid() and profile.is_valid():
            user=user.save(commit=False)
            #هش کردن پسورد
            user.set_password(user.password)
            user.save()
            profile=profile.save(commit=False)
            #برقرار رابطه ی بین پروفایل و یوزر
            profile.user=user
            profile.save()
            return redirect('user_app:home')
        #اگر فرمها معتبر نبودند،ارور های فرم ها نمایش داده شود
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
        #اگر کاربر ناشناس بود یعنی ثبت نام نکرده بود؟؟؟    
        return render(request,'user_app/login.html',context={'form':form})

    return render(request,'user_app/login.html',context={'form':form})



def profileUser(request):
    #کاربر باید احراز هویت شده باشد تا پروفایلش را ببیند!
    if request.user.is_authenticated:
        profile=userProfile.objects.get(user=request.user)
        return render(request,'user_app/profile.html',context={'profile':profile})
    #اگر احراز هویت نشده بود به صفحه لاگین منتقل شود
    return redirect ('user_app:login')

@login_required   
def editProfile(request,pk):
        #خواندن آبجکت مرتبط با آیدی درخواستی از دیتابیس
        profileObject=userProfile.objects.get(id=pk)
        profile=UserProfileForm(instance=profileObject)
        user=UserForm(instance=request.user) 

        if request.method=='POST':
            user=UserForm(request.POST or None , instance=request.user)
           
            profile=UserProfileForm(request.POST or None , instance=profileObject)
            
            if user.is_valid() and profile.is_valid():
                user.save()
                
                profile.save()
                return redirect('user_app:my_account')
            return render(request,"user_app/home.html",context={})

        return render(request,"user_app/editprofile.html",
                      context={'user':user,'profile':profile})
