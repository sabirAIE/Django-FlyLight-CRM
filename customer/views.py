from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Customer, Product, Tag, Order
from django.utils import timezone
from . import forms
from django.contrib import messages
# Create your views here.
def welcome(request):
    todays_order = Order.objects.all().count()
    delivered_order = Order.objects.filter(status="Delivered").count()
    pending_orders = Order.objects.filter(status="Pending").count()
    context = {
        'customers':Customer.objects.all(),
        'orders':Order.objects.all(),
        'todays_order':todays_order,
        'delivered_order':delivered_order,
        'pending_orders':pending_orders,
    }
    return render (request, 'customer/dashboard.html', context)

def customers(request,pk):
    customer_data = Customer.objects.get(id=pk)
    orders = customer_data.order_set.all()
    context = {
        'customer':customer_data,
        'orders':orders,
        'total_order':orders.count(),
    }
    return render(request, 'customer/customer_data.html', context)

def updateOrder(request,pk):
    order = Order.objects.filter(id=pk)
    return HttpResponse(order)

def deleteOrder(request,pk):
    order = Order.objects.filter(id=pk)
    return HttpResponse(order)

def NewOrder(request):
    return HttpResponse('hii')

def NewCustomer(request):
    customer_form = forms.createCustomer()
    if request.method == 'POST':
        form = forms.createCustomer(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Profile info updated!')
            return redirect('welcome')

    context = {
        'form': customer_form,
    }
    return render(request, 'customer/new_customer.html', context)