from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import product, cart, order
from .forms import productForm, cartForm, orderForm


class productListView(ListView):
    model = product


class productCreateView(CreateView):
    model = product
    form_class = productForm


class productDetailView(DetailView):
    model = product


class productUpdateView(UpdateView):
    model = product
    form_class = productForm


class cartListView(ListView):
    model = cart


class cartCreateView(CreateView):
    model = cart
    form_class = cartForm


class cartDetailView(DetailView):
    model = cart


class cartUpdateView(UpdateView):
    model = cart
    form_class = cartForm


class orderListView(ListView):
    model = order


class orderCreateView(CreateView):
    model = order
    form_class = orderForm


class orderDetailView(DetailView):
    model = order


class orderUpdateView(UpdateView):
    model = order
    form_class = orderForm
