from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# from django.http import HttpResponse


# Create your views here.
@login_required(login_url='log_in')
def home(request):
    return render(request,'home.html')


def register(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('log_in')
        
    return render(request,'register.html',{'form':form})

def log_in(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('home')
            
        
    return render(request,'login.html')


def log_out(request):
    logout(request)
    return redirect('log_in')

@login_required(login_url='log_in')
def change_password(request):
    form=PasswordChangeForm(user=request.user)
    if request.method=='POST':
        form=PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('log_in')
    return render(request,'change_password.html',{'form':form})
def link(request):
    return render(request,'link.html')