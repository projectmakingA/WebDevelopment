from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.urls import include,path
from django.contrib.auth import login
from .forms import TeacherRegistrationForm,StudentRegistrationForm
# Create your views here.
# users/views.py
from django.shortcuts import render, redirect

def student_register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return render(request,'registrations/stregisuccess.html')
    else:
        form = StudentRegistrationForm()
    return render(request, 'registrations/student_register.html', {'form': form})

def teacher_register(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return render(request,'registrations/trsuccess.html')
    else:
        form = TeacherRegistrationForm()
    return render(request, 'registrations/teacher_register.html', {'form': form})

def login(request):
    if(request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']
        user= auth.authenticate(username=username,password=password)
        if(user is not None):
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Enter valid username,password')
            return redirect('.')
    return render(request,'registrations/login.html')

def base(request):
    return render(request,'registrations/base.html')

def logout(request):
    auth.logout(request)
    return redirect('/')