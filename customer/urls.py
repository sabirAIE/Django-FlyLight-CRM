"""Customer URL Configuration
    Author: Sabir Ansari 
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns =[
    #navs
    path('', views.welcome, name="welcome"),

    # order urls
    path('update-order/<int:pk>', views.updateOrder, name="update-orders"),
    path('delete-order/<int:pk>', views.deleteOrder, name="delete-order"),
    path('new-order', views.newOrder, name="new-order"),
    path('customer-order/<int:pk>', views.customerOrder, name="customer-order"),

    #customer urls
    path('customer/<int:pk>', views.customers, name="customer"),
    path('new-customer', views.newCustomer, name="new-customer"),
    path('edit-customer/<int:pk>', views.editCustomer, name="edit-customer"),
    path('delete-customer/<int:pk>', views.deleteCustomer, name="delete-customer"),

]