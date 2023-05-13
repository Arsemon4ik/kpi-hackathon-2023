from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User


def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            messages.error(request, 'Your passwords are not the same, please try again')
        else:
            user = User.create(email=email, username=username, password1=password1, password2=password2)
            login(request, user)
            return redirect('admin')
    return render(request, 'authentication/register.html', {})


def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            pass
            # login(request, user)
            # return redirect('profile')
        else:
            messages.error(request, 'Incorrect email or password')
    return render(request, 'authentication/login.html', {})


@login_required
def logout_page(request):
    logout(request)
    return redirect('login')
