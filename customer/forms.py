from django import forms
from . import models
from crispy_forms import helper




class createCustomer(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = "__all__"


class createOrder(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = "__all__"