from django.contrib import admin
from django import forms
from .models import product, cart, order


class productAdminForm(forms.ModelForm):

    class Meta:
        model = product
        fields = '__all__'


class productAdmin(admin.ModelAdmin):
    form = productAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated',
                    'title', 'image', 'description', 'price']
    readonly_fields = ['created', 'last_updated']


admin.site.register(product, productAdmin)


class cartAdminForm(forms.ModelForm):

    class Meta:
        model = cart
        fields = '__all__'


class cartAdmin(admin.ModelAdmin):
    form = cartAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated']
    readonly_fields = ['name', 'created', 'last_updated']


admin.site.register(cart, cartAdmin)


class orderAdminForm(forms.ModelForm):

    class Meta:
        model = order
        fields = '__all__'


class orderAdmin(admin.ModelAdmin):
    form = orderAdminForm
    list_display = ['name', 'slug', 'created',
                    'last_updated', 'status']
    readonly_fields = ['name', 'slug', 'created', 'last_updated']


admin.site.register(order, orderAdmin)
