from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # 이메일 필드 추가

    class Meta:
        model = User  # 기본 User 모델을 사용
        fields = ('username', 'email', 'password1', 'password2')  # 비밀번호1, 비밀번호2 필드 포함
