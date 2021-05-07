from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import CharField
from django.db.models import CommaSeparatedIntegerField
from django.db.models import DateTimeField
from django.db.models import DecimalField
from django.db.models import ImageField
from django.db.models import TextField
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class product(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    title = models.TextField(max_length=512)
    image = models.ImageField(upload_to='products/', blank=True)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('app_product_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('app_product_update', args=(self.slug,))


class cart(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name="carts",
    )

    def save(self, *args, **kwargs):
        self.name = 'userId-' + str(self.user.id)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('app_cart_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('app_cart_update', args=(self.slug,))


class order(models.Model):
    PENDING = 'pending'
    SHIPPING = 'shipping'
    SHIPPED = 'shipped'

    STATUS = (
        (PENDING, PENDING),
        (SHIPPING, SHIPPING),
        (SHIPPED, SHIPPED),
    )

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    product = models.ManyToManyField(product)
    status = models.CharField(max_length=255, choices=STATUS, default=PENDING)

    # Relationship Fields
    cart = models.ForeignKey(
        'app.cart',
        on_delete=models.CASCADE, related_name="orders",
    )

    def save(self, *args, **kwargs):
        self.name = 'cartId-' + str(self.cart.id)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('app_order_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('app_order_update', args=(self.slug,))
