from django import forms
from .models import Customers, Transfer


class CustomerFrom(forms.ModelForm):
    class Meta:
        model = Customers
        fields = '__all__'


class TansferFrom(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = '__all__'
