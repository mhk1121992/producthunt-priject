from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def sign_up(request):
    if request.method == 'POST':
        # user has info and wants an account now
        if request.POST['password'] == request.POST['confirm_password']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/sign_up.html', {'error': 'This username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/sign_up.html', {'error': 'Passwords did not match!'})
    else:
        # User wants to enter info
        return render(request, 'accounts/sign_up.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Username or Password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    # TODO need to send to HOMEPAGE
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

