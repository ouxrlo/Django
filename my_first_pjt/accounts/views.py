from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm

def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # 로그인 처리 로직
            pass
    return render(request, 'accounts/login.html', {'form': form})

def signup_view(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            # 회원가입 처리 로직
            pass
    return render(request, 'accounts/signup.html', {'form': form})

