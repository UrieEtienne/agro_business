from django.urls import path
from .views import produits, produit_detail

urlpatterns = [
    path('', produits, name='produits'),
    path('<str:slug>/', produit_detail, name='produit_detail'),
]