from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import login
from . import models
from . import forms
from customer.decorators import userAuthReady

# Create your views here.
@userAuthReady
def adminLogin(request):
    if request.method == 'POST':
        user = request.POST
        email = user['email']
        password = user['password']
        if models.adminUsers.objects.filter(Q(email=email) & Q(password=password)).exists():
            user_data = models.adminUsers.objects.get(email=email)
            request.session['user_id'] = user_data.id
            messages.success(request, f'Welcome to FlyLight CRM '+ user_data.name +'!')
            return redirect('welcome')
        else:
            messages.warning(request, f'Incorrect username or password')

    context = {
        'title':"FlyLight CRM | Welcome to Admin Login",
    }
    return render(request, 'users/admin_login.html', context)


@userAuthReady
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
        'title': "FlyLight CRM | User Registration",
    }
    return render(request,'users/admin_reg.html', context)

def adminLogout(request):
    request.session.flush()
    return redirect('login')