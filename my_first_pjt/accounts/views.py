from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm, SignupForm


    

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('user_profile', username=user.username)
            else:
                form.add_error(None, '아이디 또는 비밀번호가 잘못되었습니다.')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


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


