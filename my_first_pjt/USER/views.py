from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import login as auth_login, logout
from .forms import CustomUserCreationForm

def index(request):
    return render(request, 'index.html')

def users(request):
    return render(request, 'users.html')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            auth_login(request, user)  
            return redirect('home')  
    else:
        form = CustomUserCreationForm()

    return render(request, 'USER/signup.html', {'form': form})

def login(request):
    return render(request, 'USER/login.html')




def logout_view(request):
    logout(request)  
    return redirect('home')  




@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})


