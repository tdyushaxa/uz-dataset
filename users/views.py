from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.forms import ChangeProfileForm
from users.models import Profile


# Create your views here.



class RegisterPage(View):
    def get(self,request):
        form = UserCreationForm()
        context = {
            'form':form
        }
        return render(request,'register.html',context)
    def post(self,request):
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'register.html', {"form":form})


def LoginPage(request):
    login_form = AuthenticationForm()
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('home')


    context = {
        'login_form':login_form
    }
    return render(request,'login.html',context)


def ChangeProfile(request):
    profile = request.user.profile
    form = ChangeProfileForm(instance=profile)
    if request.method == "POST":
        form = ChangeProfileForm(instance=profile,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form':form
    }
    return render(request,'chnage_profile.html',context)


def Dashboard(request):
    dashboard = request.user.profile
    context ={
        'dashboard':dashboard
    }
    return render(request,'dashboard.html',context)



def Logout(request):
    logout(request)
    return redirect('home')