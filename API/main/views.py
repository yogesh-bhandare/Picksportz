from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def organize(request):
    
    if request.method == "POST":
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        contact_number =data.get('contact_number')
        turf_name = data.get('turf_name')
        location = data.get('location')
        teammates_count = data.get('teammates_count')
        datetime = data.get('datetime')
        print(f"{first_name, last_name, contact_number, turf_name, location, teammates_count, datetime}")

        TeamMember.objects.create(
            first_name = first_name,
            last_name = last_name,
            contact_number = contact_number,
            turf_name = turf_name,
            location = location,
            teammates_count = teammates_count,
            datetime = datetime,
        )

        return redirect('/')

    return render(request, 'organize.html')

@login_required(login_url="/login/")
def join(request):
    queryset = TeamMember.objects.all()
    context = {'organize_team': queryset}
    return render(request, 'join.html', context)

def home(request):
    return render(request, 'index.html')

def logout_page(request):
    logout(request)
    return redirect('/')

def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(f"{username, password}")

        if not User.objects.filter(username = username).exists():
            messages.info(request, 'Invalid Username!')
            return redirect('/login/')
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.info(request, 'Invalid Password!')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/')
        
    return render(request, 'login.html')

def register(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(f"{first_name, last_name, username, password}")

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, 'User already registered.')
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
        )

        user.set_password(password)
        user.save()
        messages.info(request, 'Account created successfully')

        return redirect('/register/')

    
    return render(request, 'register.html')