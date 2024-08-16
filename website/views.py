from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import FileResponse, Http404
from django.conf import settings
import os
from django.contrib.auth.decorators import login_required
#from .forms import SignUpForm


# Create your views here.
def home(request):
    
        return render(request,'home.html',{})
    
def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'dashboard.html',{})
    else:
        messages.success(request,"You Must Be Logged In To View This Page.....")
        return redirect('login')

def login_user(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            #messages.success(request,"You Have Been Logged In")
            return redirect('dashboard')
        else:
            messages.success(request,"There Was An Error Logging In, Please Try Again....")
            return redirect('login')
    else:
        return render(request,'login.html',{})

# def register_user(request):
#     if request.method=='POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(username=username,password=password)
#             login(request,user)
#             messages.success(request,"You Have Successfully Registered...!")
#             return redirect('home')
#     else:
#         form = SignUpForm()
#         return render(request,'register.html',{'form':form})
#     return render(request,'register.html',{'form':form})

def logout_user(request):
    logout(request)
    messages.success(request,"You Have Been Logged Out.....")
    return redirect('home')

from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

def protected_media(request, path):
    if request.user.is_authenticated:
        file_path = BASE_DIR / 'media' /path
        print(file_path)
        if os.path.exists(file_path):
            
            return FileResponse(open(file_path,'rb'),content_type='application/pdf')
        else:
            raise Http404("File does not exist")
    else:
        messages.success(request,"You Must Be Logged In To View This Page.....")
        return redirect('login')