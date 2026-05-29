from django.db import models
import uuid


class Paiement(models.Model):

    METHODES = (

        ('orange_money', 'Orange Money'),

        ('mtn_money', 'MTN Mobile Money'),

    )

    STATUTS = (

        ('en_attente', 'En attente'),

        ('succes', 'Succès'),

        ('echec', 'Échec'),

    )

    qr_code = models.ImageField(
        upload_to='paiements_qr/',
        blank=True,
        null=True
    )

    reference = models.CharField(
        max_length=100,
        unique=True,
        blank=True
    )

    client_nom = models.CharField(
        max_length=255
    )

    telephone = models.CharField(
        max_length=30
    )

    montant = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    methode = models.CharField(
        max_length=50,
        choices=METHODES
    )

    statut = models.CharField(
        max_length=30,
        choices=STATUTS,
        default='en_attente'
    )

    transaction_id = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    date_creation = models.DateTimeField(
        auto_now_add=True
    )

    def save(self, *args, **kwargs):

        if not self.reference:

            self.reference = (
                uuid.uuid4()
                .hex[:10]
                .upper()
            )

        super().save(*args, **kwargs)

    def __str__(self):

        return self.reference