import django_filters
from django.forms import TextInput, NumberInput
from django_filters import CharFilter

from .models import Customers


class Search(django_filters.FilterSet):
    name = CharFilter(field_name=['name', 'id'], lookup_expr='icontains')
    id = CharFilter(field_name='id', lookup_expr='icontains')
    widgets = {
        'name': CharFilter(attrs={
            'class': "form-control",
            'style': 'max-width: 300;',
            'placeholder': 'Name'
        }),
        'id': CharFilter(attrs={
            'class': "form-control",
            'style': 'max-width: 300;',
            'placeholder': 'Name'
        }),
    }

    class Meta:
        model = Customers
        fields = '__all__'
        exclude = ['surname', 'email', 'phone_number', 'address', 'date_created']