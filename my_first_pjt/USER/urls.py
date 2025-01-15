from django.urls import path, include
from django.contrib.auth import views as auth_views, logout
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('users/', views.users, name='users'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='USER/login.html'), name='login'),
    path('home/', views.index, name='home'),
]
