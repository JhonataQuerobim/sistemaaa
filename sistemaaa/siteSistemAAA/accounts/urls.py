from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done, password_reset_confirm,
    password_reset_complete
)

urlpatterns = [
    path('', views.home, name='home'),
    path('home_admin', views.home_admin, name='home_admin'),
    path('login/', login, {'template_name': 'accounts/login.html'}, name='login'),
    path('client_list/', views.client_list, name='client_list'),
    path('register/', views.register, name='register'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]