from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
from django.contrib import auth


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        
        User=get_user_model()
        
        if User.objects.filter(email=email).exists():        
            messages.info(request, "Email already registered")
            return redirect('register')
        else:
            # User.objects.create_user(name=name, email=email, password=make_password(password))   
            User.objects.create_user(name=name, email=email, password=password)   
            messages.info(request, "Registration successful")
            return redirect("/")
            
    else:
        return render(request, 'register.html')
      
      
def login(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']

        User=get_user_model()

        if User.objects.filter(email=email).exists():   
            user=auth.authenticate(email=email, password=password)
            if user is not None:
                auth.login(request,user)        
                messages.info(request, "Login successful")
                return redirect('/')
            else:
                messages.info(request, "Invalid Credentials ")
                return redirect('login')                    
        else:
            messages.info(request, "Email does not exist")
            return redirect("/")
    else:
        return render(request, 'login.html')
    

def logout(request):
    auth.logout(request)
    return redirect("/")


# ! -------------------------------------------------------------------------------------
# def register(request):
#     if request.method == 'POST':
#         name=request.POST['name']
#         email=request.POST['email']
#         password=request.POST['password']

#         if CustomUser.objects.filter(email=email).exists():        
#             messages.info(request, "Email already registered")
#             return redirect('register')
#         else:
#             user = CustomUser.objects.create(name=name, email=email, password=make_password(password))   
#             user.save()
#             messages.info(request, "Registration successful")
#             return redirect("/")
            
#     else:
#         return render(request, 'register.html')
      
      
# def login(request):
#     if request.method == 'POST':
#         email=request.POST['email']
#         password=request.POST['password']

#         print(email, password)

#         if CustomUser.objects.filter(email=email).exists():        
#             user = CustomUser.objects.get(email=email)   
#             if check_password(password,user.password):            
#                 messages.info(request, "Login successful")
#                 return redirect('/')
#             else:
#                 messages.info(request, "Password does not match")
#                 return redirect('login')
#         else:
#             messages.info(request, "Email does not exist")
#             return redirect("/")
#     else:
#         return render(request, 'login.html')
    

# ! -------------------------------------------------------------------------------------