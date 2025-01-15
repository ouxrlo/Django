from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def users(request):
    return render(request, 'user.html')

def signup(request):
    return render(request, 'signup.html')