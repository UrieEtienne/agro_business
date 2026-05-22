from django.shortcuts import render, get_object_or_404
from .models import Product


# LISTE PRODUITS

def products(request):

    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(
        request,
        'products/products.html',
        context
    )


# DETAIL PRODUIT

def product_detail(request, id):

    product = get_object_or_404(
        Product,
        id=id
    )

    context = {
        'product': product
    }

    return render(
        request,
        'products/product_detail.html',
        context
    )