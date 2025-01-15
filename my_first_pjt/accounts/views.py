from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm, SignupForm



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'USER/login.html', {'form': form})



def logout_view(request):
    logout(request)  
    return redirect('index') 

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            
            user = form.save()
            login(request, user)
            
            
            return redirect('user_profile', username=user.username)
    else:
        form = SignupForm()
    
    return render(request, 'accounts/signup.html', {'form': form})




def user_profile(request, username):
    user = User.objects.get(username=username) 
    return render(request, 'accounts/user_profile.html', {'user': user})


