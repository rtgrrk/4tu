import unittest
from django.urls import reverse
from django.test import Client
from .models import product, cart, order
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_product(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["title"] = "title"
    defaults["image"] = "image"
    defaults["description"] = "description"
    defaults["price"] = "price"
    defaults.update(**kwargs)
    return product.objects.create(**defaults)


def create_cart(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    if "user" not in defaults:
        defaults["user"] = create_django_contrib_auth_models_user()
    return cart.objects.create(**defaults)


def create_order(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["status"] = "status"
    defaults.update(**kwargs)
    if "cart" not in defaults:
        defaults["cart"] = create_cart()
    return order.objects.create(**defaults)


class productViewTest(unittest.TestCase):
    '''
    Tests for product
    '''
    def setUp(self):
        self.client = Client()

    def test_list_product(self):
        url = reverse('app_product_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_product(self):
        url = reverse('app_product_create')
        data = {
            "name": "name",
            "title": "title",
            "image": "image",
            "description": "description",
            "price": "price",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_product(self):
        product = create_product()
        url = reverse('app_product_detail', args=[product.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_product(self):
        product = create_product()
        data = {
            "name": "name",
            "title": "title",
            "image": "image",
            "description": "description",
            "price": "price",
        }
        url = reverse('app_product_update', args=[product.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class cartViewTest(unittest.TestCase):
    '''
    Tests for cart
    '''
    def setUp(self):
        self.client = Client()

    def test_list_cart(self):
        url = reverse('app_cart_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_cart(self):
        url = reverse('app_cart_create')
        data = {
            "name": "name",
            "user": create_django_contrib_auth_models_user().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_cart(self):
        cart = create_cart()
        url = reverse('app_cart_detail', args=[cart.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_cart(self):
        cart = create_cart()
        data = {
            "name": "name",
            "user": create_django_contrib_auth_models_user().pk,
        }
        url = reverse('app_cart_update', args=[cart.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class orderViewTest(unittest.TestCase):
    '''
    Tests for order
    '''
    def setUp(self):
        self.client = Client()

    def test_list_order(self):
        url = reverse('app_order_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_order(self):
        url = reverse('app_order_create')
        data = {
            "name": "name",
            "status": "status",
            "cart": create_cart().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_order(self):
        order = create_order()
        url = reverse('app_order_detail', args=[order.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_order(self):
        order = create_order()
        data = {
            "name": "name",
            "status": "status",
            "cart": create_cart().pk,
        }
        url = reverse('app_order_update', args=[order.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


