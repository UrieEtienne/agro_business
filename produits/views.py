from django.shortcuts import render
from .models import Produit


def produits(request):

    produits_list = Produit.objects.filter(
        disponible=True
    ).order_by('-created_at')

    return render(
        request,
        "produits/produits.html",
        {
            "produits": produits_list
        }
    )