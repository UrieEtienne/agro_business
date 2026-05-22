from django.urls import path
from .views import products, product_detail

urlpatterns = [
    path('', products, name='products'),
    path('<str:slug>/', product_detail, name='product_detail'),
]