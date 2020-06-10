from django import forms
from . import models

class registrationForm(forms.ModelForm):
    class Meta:
        model = models.adminUsers
        fields = "__all__"
        exclude = ['phone']