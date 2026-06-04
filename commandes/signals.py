from django.db.models.signals import post_save
from django.dispatch import receiver
from commandes.models import Commande
from factures.models import Facture
import uuid


@receiver(post_save, sender=Commande)
def create_facture(sender, instance, created, **kwargs):

    if created:

        Facture.objects.create(
            commande=instance,

            client_nom=instance.nom_client,
            telephone=instance.telephone,
            adresse=instance.adresse,

            produit=str(instance.produit),
            quantite=instance.quantite,
            prix_unitaire=instance.produit.prix,

            statut="en_attente"
        )