from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def index(request):
    return render(request, 'index.html')

def users(request):
    return render(request, 'users.html')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # 폼에서 데이터를 저장
            login(request, user)  # 자동 로그인
            return redirect('home')  # 회원가입 후 홈 화면으로 리디렉션
    else:
        form = CustomUserCreationForm()

    return render(request, 'user/signup.html', {'form': form})

def login(request):
    return render(request, 'USER/login.html')

