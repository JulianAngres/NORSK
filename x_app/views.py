from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    context = {}
    return render(request, 'x_app/index.html', context)

def loginPage(request):
    print('Helloooo')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/calendar/')
        else:
            messages.info(request, 'Username or Password Incorrect')
            return render(request, 'login.html')

    return render(request, 'login.html')

def pleese_verify(request):
    return render(request, 'users/pleese_verify.html')

def success_verification(request):
    return render(request, 'users/success_verification.html')

def password_reset_complete(request):
    return render(request, 'users/password_reset_complete.html')