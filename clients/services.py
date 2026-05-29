from commandes.models import Commande


def historique_achats(client):

    commandes = Commande.objects.filter(

        client=client

    ).order_by(

        '-date_commande'

    )

    return commandes