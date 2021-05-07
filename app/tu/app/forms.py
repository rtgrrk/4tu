from django import forms
from .models import product, cart, order


class productForm(forms.ModelForm):
    class Meta:
        model = product
        fields = ['name', 'title', 'image', 'description', 'price']


class cartForm(forms.ModelForm):
    class Meta:
        model = cart
        fields = ['name', 'user']


class orderForm(forms.ModelForm):
    class Meta:
        model = order
        fields = ['name', 'status', 'cart']
