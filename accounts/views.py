from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    if request.method == 'POST':
        
        # User Registration
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check if passwords match
        if password == password2:
            # check Username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is taken')
                return redirect('register')
            else:
                # check if email has been used t register another account
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Account with that email already exists')
                    return redirect('register')
                else:
                     user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name ) 
                     # Login after registration  
                    #  auth.login(request, user)
                    #  messages.success(request, 'You are now logged in')
                    #  return redirect('index')

                    #  redirect to login page after registration
                     user.save()
                     messages.success(request, 'You are now registered')
                     return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')

        return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        # User Login
        return 
    else:
        return render(request, 'accounts/login.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def logout(request):
    return redirect('index')    