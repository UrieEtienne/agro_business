from django.shortcuts import render
from .models import Promotion

def accueil_shop(request):

    promotions = Promotion.objects.filter(
        active=True
    ).order_by('-created_at')[:3]

    context = {
        'promotions': promotions
    }

    return render(
        request,
        'ecommerce/accueil_shop.html',
        context
    )


def boutique(request):

    promotions = Promotion.objects.filter(
        active=True
    )

    context = {
        'promotions': promotions
    }

    return render(
        request,
        'ecommerce/boutique.html',
        context
    )