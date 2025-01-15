from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm, SignupForm


# 로그인 뷰
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)  # LoginForm을 사용하여 POST 데이터 받기
        if form.is_valid():
            # form.cleaned_data에서 유효한 데이터를 받아옴
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # 사용자 인증
            user = authenticate(username=username, password=password)
            
            if user is not None:
                # 사용자가 인증되면 로그인 처리
                login(request, user)
                return redirect('index')  # 로그인 후 리디렉션할 URL, 'index'로 설정
            else:
                form.add_error(None, '아이디 또는 비밀번호가 맞지 않습니다.')
    else:
        form = LoginForm()  # GET 요청 시 폼을 초기화

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


