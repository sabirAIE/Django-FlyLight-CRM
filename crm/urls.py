"""crm URL Configuration
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls,name="admin"),
    #Customer Route
    path('', include('customer.urls'), name="root"),
    #User Route
    path('user/', include('users.urls'), name="user"),
]
