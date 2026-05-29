from django.db.models import Sum
from .models import Paiement
from django.shortcuts import render
from .mobile_money import (
    generate_orange_payment
)


def paiement_page(request):

    if request.method == 'POST':

        paiement = Paiement.objects.create(

            client_nom=request.POST.get(
                'client_nom'
            ),

            telephone=request.POST.get(
                'telephone'
            ),

            montant=request.POST.get(
                'montant'
            ),

            methode=request.POST.get(
                'methode'
            )

        )

        response = generate_orange_payment(
            paiement
        )

        return render(

            request,

            'paiements/success.html',

            {

                'response': response

            }

        )

    return render(

        request,

        'paiements/paiement.html'
    )

# DASHBOARD FINANCIER
def dashboard_financier(request):

    total_revenus = Paiement.objects.filter(
        statut='succes'
    ).aggregate(
        Sum('montant')
    )

    paiements = Paiement.objects.all()

    return render(

        request,

        'paiements/dashboard.html',

        {

            'total_revenus': total_revenus,

            'paiements': paiements

        }

    )