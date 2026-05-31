from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Commande
from factures.models import Facture
import uuid

@receiver(post_save, sender=Commande)
def create_facture(sender, instance, created, **kwargs):

    if created:

        Facture.objects.create(
            numero=f"FAC-{uuid.uuid4().hex[:6].upper()}",
            commande=instance,
            statut="en_attente"
        )