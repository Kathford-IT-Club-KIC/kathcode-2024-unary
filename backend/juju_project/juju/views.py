# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as AuthUser
from .models import User,RestaurantOwner
from django.db import IntegrityError

def home(request):
    return render(request, 'index.html')

def map(request):
        query= RestaurantOwner.objects.all()

    # Retrieve cart items from localStorage or any storage mechanism
        return render(request, 'map.html',{'data':query})

def menu(request):
    return render(request, 'menu.html')

def ownerorderdetails(request):
    return render(request, 'ownerorderdetails.html')

def cart_view(request):
     return render(request, 'cart.html')

def ownerhome(request):
    return render(request, 'ownerhome.html')

def user_login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_dashboard')
        else:
            return render(request, 'userlogin.html', {'error': 'Invalid credentials'})
    return render(request, 'userlogin.html')

@login_required
def user_dashboard(request):
    user = User.objects.get(email=request.user.email)
    return render(request, 'userdashboard.html', {'user': user})

def owner_login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('owner_dashboard')
        else:
            return render(request, 'ownerlogin.html', {'error': 'Invalid credentials'})
    return render(request, 'ownerlogin.html')

@login_required
def owner_dashboard(request):
    user = User.objects.get(email=request.user.email)
    return render(request, 'ownerdashboard.html', {'user': user})

def signup_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']

        try:
            # Create Django's built-in User model instance
            auth_user = AuthUser.objects.create_user(username=email, email=email, password=password)
            
            # Create custom User model instance
            User.objects.create(
                name=name,
                email=email,
                latitude=latitude,
                longitude=longitude
            )
            
            # Log the user in
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('userlogin')
        
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'Email already exists'})
        
    return render(request, 'signup.html')



