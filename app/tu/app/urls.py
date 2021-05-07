from django.urls import path, re_path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'product', api.productViewSet)
router.register(r'cart', api.cartViewSet)
router.register(r'order', api.orderViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/', include(router.urls)),
)

urlpatterns += (
    # urls for Django Rest Framework API
    re_path(r'^$', views.HomeView.as_view(), name='home'),
)

urlpatterns += (
    # urls for product
    path('product/', views.productListView.as_view(), name='app_product_list'),
    path('product/create/', views.productCreateView.as_view(),
         name='app_product_create'),
    path('product/detail/<slug:slug>/',
         views.productDetailView.as_view(), name='app_product_detail'),
    path('product/update/<slug:slug>/',
         views.productUpdateView.as_view(), name='app_product_update'),
)

urlpatterns += (
    # urls for cart
    path('cart/', views.cartListView.as_view(), name='app_cart_list'),
    path('cart/create/', views.cartCreateView.as_view(), name='app_cart_create'),
    path('cart/detail/<slug:slug>/',
         views.cartDetailView.as_view(), name='app_cart_detail'),
    path('cart/update/<slug:slug>/',
         views.cartUpdateView.as_view(), name='app_cart_update'),
)

urlpatterns += (
    # urls for order
    path('order/', views.orderListView.as_view(), name='app_order_list'),
    path('order/create/', views.orderCreateView.as_view(),
         name='app_order_create'),
    path('order/detail/<slug:slug>/',
         views.orderDetailView.as_view(), name='app_order_detail'),
    path('order/update/<slug:slug>/',
         views.orderUpdateView.as_view(), name='app_order_update'),
)
