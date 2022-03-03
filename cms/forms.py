from django.forms import ModelForm, TextInput, EmailInput
from .models import Customers


class CustomersForm(ModelForm):

    class Meta:
        model = Customers
        fields = ['name', 'surname', 'email', 'phone_number', 'address', ]
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
            }),
            'surname': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'surname'
            }),
            'phone_number': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'phone_number'
            }),

            'email': EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
            })
            ,
            'address': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'address'
            }),
        }