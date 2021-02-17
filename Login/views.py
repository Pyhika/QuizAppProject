from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import ProfileModel


def signupview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        try:
            User.objects.create_user(username_data, '', password_data)
            return redirect('login')
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーはすでに登録されています'})
    else:
        return render(request, 'signup.html', {})


def loginview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        user = authenticate(request, username=username_data, password=password_data)

        if user is not None:
            login(request, user)
            return redirect('top')
        else:
            return redirect('login')
    return render(request, 'login.html')


@login_required
def topview(request):
    object_list = ProfileModel.objects.all()
    return render(request, 'top.html', {'object_list': object_list})


def logoutview(request):
    logout(request)
    return redirect('login')
