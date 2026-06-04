from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.produits,
        name='produits'
    ),

    path('categorie/<slug:slug>/', views.categorie_detail, name='categorie_detail')

]