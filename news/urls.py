from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import PasswordsChangeView, PasswordResetView

urlpatterns = [
    path('', views.home_view, name='home'),
    #path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('', include('django.contrib.auth.urls')),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/password_reset.html')),
    path('password/', PasswordsChangeView.as_view(template_name='registration/password_change.html')),
    path('reset_password/', PasswordResetView.as_view(template_name='registration/password_reset.html')),
    path('password_success/', views.password_success, name='password_success'),
    path('reset_passwords/sent/', views.password_reset_done),
]