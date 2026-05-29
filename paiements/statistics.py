from django.db.models import Sum
from .models import Paiement


def revenus_par_mois():

    return Paiement.objects.filter(
        statut='succes'
    ).aggregate(
        Sum('montant')
    )