from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Customer, Product, Tag, Order
from django.utils import timezone
from . import forms
from django.contrib import messages
from . import filters

# Create your views here.
def welcome(request):
    todays_order = Order.objects.all().count()
    delivered_order = Order.objects.filter(status="Delivered").count()
    pending_orders = Order.objects.filter(status="Pending").count()
    orders = Order.objects.all()
    order_filter = filters.orderFilters(request.GET, queryset=orders)
    if request.method =='GET':
        orders = order_filter.qs
        
    context = {
        'customers':Customer.objects.all(),
        'orders':orders,
        'todays_order':todays_order,
        'delivered_order':delivered_order,
        'pending_orders':pending_orders,
        'order_filter':order_filter
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
    order = Order.objects.get(id=pk)
    updateOrder_form = forms.createOrder(instance=order)

    if request.method == 'POST':
        form = forms.createOrder(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request,f'Order info Updated!')
            return redirect('welcome')

    context = {
        'form':updateOrder_form
    }
    return render(request, 'customer/update_order.html', context)

def deleteOrder(request,pk):
    order_data = Order.objects.get(id=pk)

    if request.method =='POST':
        order_data.delete()
        messages.success(request,f'Order info deleted!')
        return redirect('welcome')

    context={
        'order':order_data,
    }
    return render(request, 'customer/delete_order.html', context)

def newOrder(request):

    if request.method == 'POST':
        form = forms.createOrder(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Order Created')
            return redirect('welcome')
    context = {
        'form':forms.createOrder()
    }

    return render(request, 'customer/new_order.html', context)

def customerOrder(request,pk):
    customer_data = Customer.objects.get(id=pk)
    order_form = forms.createOrder(initial={'customer':customer_data})
    if request.method == 'POST':
        form = forms.createOrder(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Order Created')
            return redirect('customer',pk=pk)
            
    context = {
        'form':order_form
    }

    return render(request, 'customer/new_order.html', context)

def newCustomer(request):
    customer_form = forms.createCustomer()
    if request.method == 'POST':
        form = forms.createCustomer(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Profile info Created!')
            return redirect('welcome')

    context = {
        'form': customer_form,
    }
    return render(request, 'customer/new_customer.html', context)

def editCustomer(request,pk):
    customer_data = Customer.objects.get(id=pk)
    edit_customer_form = forms.createCustomer(instance=customer_data)

    if request.method == 'POST':
        form = forms.createCustomer(request.POST,instance=customer_data)
        if form.is_valid():
            form.save()
            messages.success(request,f'Profile info updated!')
            return redirect('welcome')

    context = {
        'form':edit_customer_form,
    }
    return render(request, 'customer/new_customer.html', context)

def deleteCustomer(request,pk):
    customer_data = Customer.objects.get(id=pk)

    if request.method =='POST':
        customer_data.delete()
        messages.success(request,f'Profile info deleted!')
        return redirect('welcome')

    context = {
        'customer': customer_data,
    }
    return render(request, 'customer/delete_customer.html', context)