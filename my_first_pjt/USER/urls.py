from django.urls import path, include
from django.contrib.auth import views as auth_views, logout
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('users/', views.users, name='users'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('home/', views.index, name='home'),
]
