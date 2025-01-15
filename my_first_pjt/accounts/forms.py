from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User




class USERForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField()


# 사용자 가입을 위한 폼 정의
class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']




# 로그인 폼을 커스터마이징하려면 AuthenticationForm을 상속해서 사용해
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
