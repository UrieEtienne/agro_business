from .models import Stock


def get_alertes_stock():

    return Stock.objects.filter(

        quantite__lte=models.F(
            'seuil_alerte'
        )

    )