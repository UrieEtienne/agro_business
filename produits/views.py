from django.shortcuts import render
from .models import Produit, Categorie

def produits(request):

    categories = Categorie.objects.prefetch_related('produits').all()

    produits_list = Produit.objects.filter(
        disponible=True
    ).order_by('-created_at')

    return render(
        request,
        "produits/produits.html",
        {
            "categories": categories,
            "produits": produits_list,
        }
    )

def categorie_detail(request, slug):

    categorie = Categorie.objects.get(slug=slug)

    return render(request, "produits/categorie.html", {
        "categorie": categorie
    })