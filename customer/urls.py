"""Customer URL Configuration
    Author: Sabir Ansari 
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns =[
    path('', views.welcome, name="welcome"),

    path('update-order/<int:pk>', views.updateOrder, name="update-orders"),
    path('delete-order/<int:pk>', views.deleteOrder, name="delete-order"),
    path('customer/<int:pk>', views.customers, name="customer"),
    path('new-order', views.NewOrder, name="new-order"),
    path('new-customer', views.NewCustomer, name="new-customer"),
]