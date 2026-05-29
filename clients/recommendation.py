from boutique.models import Produit
from favoris.models import Favori


def recommander_produits(client):

    # RECUPERER LES FAVORIS DU CLIENT
    favoris = Favori.objects.filter(
        client=client
    ).select_related(
        'produit',
        'produit__categorie'
    )

    # RECUPERER LES IDS DES PRODUITS FAVORIS
    produits_favoris_ids = favoris.values_list(
        'produit_id',
        flat=True
    )

    # RECUPERER LES IDS DES CATEGORIES FAVORITES
    categories_ids = favoris.values_list(
        'produit__categorie_id',
        flat=True
    ).distinct()

    # RECOMMANDATIONS
    recommandations = Produit.objects.filter(

        categorie_id__in=categories_ids

    ).exclude(

        id__in=produits_favoris_ids

    ).distinct()[:8]

    return recommandations