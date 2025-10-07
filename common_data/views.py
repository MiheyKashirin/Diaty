from urllib import request
from django.contrib.auth import logout as django_logout
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'profile.html')



def login_handler(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')



def logout_handler(request):
    logout(request)
    return redirect('login')

def register_handler(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        try:
            User.objects.get(username=username)
            return render(request, 'register.html', {'error': 'Username already exists'})
        except User.DoesNotExist:
            pass
        new_user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        new_user.save()
        return redirect('/login')
    else:
        return render(request, 'register.html')
