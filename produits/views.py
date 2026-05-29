from django.shortcuts import render
from .models import Produit


def produits(request):

    produits = Produit.objects.filter(
        disponible=True
    ).order_by('-created_at')

    return render(
        request,
        'produits.html',
        {
            'produits': produits
        }
    )