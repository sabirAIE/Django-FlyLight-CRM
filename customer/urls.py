"""Customer URL Configuration
    Author: Sabir Ansari 
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from users import views as userViews

urlpatterns =[
    #app navs
    path('', views.welcome, name="welcome"),
    path('user/login', userViews.adminLogin, name='user'),
    path('user/logout', userViews.adminLogout, name="user-logout"),
    # order urls
    path('update-order/<int:pk>', views.updateOrder, name="update-orders"),
    path('delete-order/<int:pk>', views.deleteOrder, name="delete-order"),
    path('customer-order/<int:pk>', views.customerOrder, name="customer-order"),
    path('orders', views.allOrders, name="all-orders"),

    #customer urls
    path('customer/<int:pk>', views.customers, name="customer"),
    path('new-customer', views.newCustomer, name="new-customer"),
    path('edit-customer/<int:pk>', views.editCustomer, name="edit-customer"),
    path('delete-customer/<int:pk>', views.deleteCustomer, name="delete-customer"),
    path('all-customers', views.allCustomers, name="all-customers"),

]