from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.db.models import Q
from . import models
from . import forms
# Create your views here.
def adminLogin(request):
    if request.method == 'POST':
        user = request.POST
        email = user['email']
        password = user['password']
        if models.adminUsers.objects.filter(Q(email=email) & Q(password=password)).exists():
            user_data = models.adminUsers.objects.get(email=email)
            messages.success(request, f'Welcome to FlyLight CRM '+ user_data.name +'!')
            return redirect('welcome')
        else:
            messages.warning(request, f'Incorrect username or password')

    context = {
        'title':"Welcome to Admin Login",
    }
    return render(request, 'users/admin_login.html', context)

def userRegistration(request):
    if request.method == 'POST':
        user_data = request.POST
        if user_data['password'] == user_data['password1']:
            if models.adminUsers.objects.filter(email=user_data['email']).exists():
                messages.warning(request, f'Email Id allredy exist')
            else:
                form = forms.registrationForm(user_data)
                if form.is_valid():
                    messages.success(request, f'Account has been created')
                    form.save()
                    return redirect('login')
                else:
                    messages.warning(request, f'Form is not Validated')
        else:
            messages.warning(request, f'Password did not match')

    context = {
        'title': "User Registration",
    }
    return render(request,'users/admin_reg.html', context)