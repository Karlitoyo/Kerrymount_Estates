from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'phone_number', 'email', 'address_line1',
                 'address_line2', 'town_or_city', 'post_code', 'country')
