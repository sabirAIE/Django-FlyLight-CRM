"""Customer URL Configuration
    Author: Sabir Ansari 
"""
from django.urls import path, include
from . import views

urlpatterns = [
    #login
    path('', views.adminLogin, name="admin-login"),
    path('registration', views.userRegistration, name="admin-register"),
    path('login', views.adminLogin, name="login"),
]