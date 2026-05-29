from .models import (

    Stock,
    MouvementStock

)


def ajouter_stock(stock, quantite):

    stock.quantite += quantite

    stock.save()

    MouvementStock.objects.create(

        stock=stock,

        type_mouvement='entree',

        quantite=quantite

    )


def retirer_stock(stock, quantite):

    if stock.quantite >= quantite:

        stock.quantite -= quantite

        stock.save()

        MouvementStock.objects.create(

            stock=stock,

            type_mouvement='sortie',

            quantite=quantite

        )