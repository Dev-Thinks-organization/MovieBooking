from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import *
from django.contrib.auth import get_user_model


User = get_user_model()


def signin(request):
    context = {}
    nxt = request.GET.get('next', None)
    if request.user.is_authenticated:
        redirect('/')
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            print('the user is Login')
            return redirect('movies')

    return render(request, 'SignIn.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('/')


def register(request):
    context = {}
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(email=email, password=password
                                        )
        if user is not None:
            auth_login(request, user)
            return redirect('movies')

    return render(request, 'SignUp.html', context=context)
