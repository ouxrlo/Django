from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('users/', views.users, name='users'),
    path('login/', views.login, name='login'),
]
