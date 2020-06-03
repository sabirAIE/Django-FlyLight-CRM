from django import forms
from .models import Customer
from crispy_forms import helper




class createCustomer(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields = "__all__"

