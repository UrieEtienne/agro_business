from django.shortcuts import render

from .models import (

    Stock,
    MouvementStock

)

from .utils import get_alertes_stock


def liste_stocks(request):

    stocks = Stock.objects.all()

    return render(

        request,

        'stocks/liste_stocks.html',

        {

            'stocks': stocks

        }

    )


def alertes_stock(request):

    alertes = get_alertes_stock()

    return render(

        request,

        'stocks/alertes_stock.html',

        {

            'alertes': alertes

        }

    )


def mouvements_stock(request):

    mouvements = MouvementStock.objects.all().order_by(

        '-date_mouvement'

    )

    return render(

        request,

        'stocks/mouvements_stock.html',

        {

            'mouvements': mouvements

        }

    )