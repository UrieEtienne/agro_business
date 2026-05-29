from django.shortcuts import render, get_object_or_404
from .models import Product


# LISTE PRODUITS

def produits(request):

    produits = Product.objects.all()

    context = {
        'produits': produits
    }

    return render(
        request,
        'produits/produits.html',
        context
    )


# DETAIL PRODUIT

def produit_detail(request, id):

    produit = get_object_or_404(
        Product,
        id=id
    )

    context = {
        'produit': produit
    }

    return render(
        request,
        'produits/produit_detail.html',
        context
    )