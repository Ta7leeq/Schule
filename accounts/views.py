from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with the name of your home view
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid username or password'})
    return render(request, 'accounts/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
