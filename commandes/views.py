from django.shortcuts import render
from .models import Commande


def liste_commandes(request):

    commandes = Commande.objects.all().order_by(
        '-date_commande'
    )

    return render(
        request,
        'commandes/liste_commandes.html',
        {
            'commandes': commandes
        }
    )