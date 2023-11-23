from django.shortcuts import render,redirect
from django.contrib.auth.models import  auth
from .models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password

def home(request):
    return render(request, 'base.html')
    
def register(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']

        if User.objects.filter(email=email).exists():        
            messages.info(request, "Email already registered")
            return redirect('register')
        else:
            user = User.objects.create(name=name, email=email, password=make_password(password))   
            user.save()
            messages.info(request, "Registration successful")
            return redirect("/")
            
    else:
        return render(request, 'register.html')
    
    
def login(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']

        print(email, password)

        if User.objects.filter(email=email).exists():        
            user = User.objects.get(email=email)   
            if check_password(password,user.password):            
                messages.info(request, "Login successful")
                return redirect('/')
            else:
                messages.info(request, "Password does not match")
                return redirect('login')
        else:
            messages.info(request, "Email does not exist")
            return redirect("/")
    else:
        return render(request, 'login.html')
    
    
def registerAdmin(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']

        if User.objects.filter(email=email).exists():        
            messages.info(request, "Email already registered")
            return redirect('register')
        else:
            user = User.objects.create(name=name, email=email, password=make_password(password))   
            user.save()
            messages.info(request, "Registration successful")
            return redirect("/")
            
    else:
        return render(request, 'register.html')
    
    
def loginAdmin(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']

        print(email, password)

        if User.objects.filter(email=email).exists():        
            user = User.objects.get(email=email)   
            if check_password(password,user.password):            
                messages.info(request, "Login successful")
                return redirect('/')
            else:
                messages.info(request, "Password does not match")
                return redirect('login')
        else:
            messages.info(request, "Email does not exist")
            return redirect("/")
    else:
        return render(request, 'login.html')
    
    
    