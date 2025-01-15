from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    path('login/', views.login_view, name='login'),  # 로그인 URL 경로 설정
    
]
