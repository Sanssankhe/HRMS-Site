from django import forms
from django.core.checks import messages
from django.shortcuts import redirect, render
from hr import models
from django.contrib.auth.models import User , auth
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UsernameField
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        desc=request.POST['desc']
        print(name, email, desc)
        print("This is post")
        ins = models.contact(name=name, email=email, desc=desc)
        ins.save()
        print("The data is stored")

    return render(request, 'contact.html')

@login_required
def employee(request):
    return render(request, 'employee.html')
def task(request):
    if request.method== 'POST':
        desc=request.POST['desc']
        nam=request.POST['nam']
        print(desc, nam)
        ins = models.task(desc=desc, nam=nam)
        ins.save()
        print("The data is stored")
    return render(request, 'task.html')
def leave(request):
    if request.method=='POST':
        name= request.POST['name']
        email = request.POST['email']
        leavetype= request.POST['leavetype']
        datestart= request.POST['datestart']
        dateend= request.POST['dateend']
        reason= request.POST['reason']
        halfday= request.POST['halfday']
        ins = models.leave(name=name, email=email, leavetype=leavetype, datestart=datestart, dateend=dateend, reason= reason, halfday= halfday)
        ins.save()
    return render(request, 'leave.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        
        user= User.objects.create_user(username=username, password=password)
        user.save();
        print("User created")
        return redirect('/login')
    else: 
        return render(request, 'register.html')
def login(request):        
    return render(request, 'login.html')    
def logout(request):
    return render(request, 'logout.html')
def dash(request):
    return render(request, 'index.html')
def log(request):
    return render(request, 'log.html')