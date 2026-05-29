from django.db import models


# =========================
# CLIENT
# =========================

class Client(models.Model):

    nom = models.CharField(
        max_length=255
    )

    telephone = models.CharField(
        max_length=50
    )

    adresse = models.TextField()

    email = models.EmailField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nom


# =========================
# COMMANDE
# =========================

class Commande(models.Model):

    STATUT_CHOICES = [

        ('en_attente', 'En attente'),

        ('validee', 'Validée'),

        ('en_livraison', 'En livraison'),

        ('livree', 'Livrée'),

        ('annulee', 'Annulée'),
    ]

    PAIEMENT_CHOICES = [

        ('non_paye', 'Non payé'),

        ('paye', 'Payé'),

        ('partiel', 'Paiement partiel'),
    ]

    numero_commande = models.CharField(
        max_length=100,
        unique=True
    )

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='commandes'
    )

    date_commande = models.DateTimeField(
        auto_now_add=True
    )

    montant_total = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    statut = models.CharField(
        max_length=50,
        choices=STATUT_CHOICES,
        default='en_attente'
    )

    paiement = models.CharField(
        max_length=50,
        choices=PAIEMENT_CHOICES,
        default='non_paye'
    )

    commentaire = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.numero_commande


# =========================
# LIGNE COMMANDE
# =========================

class LigneCommande(models.Model):

    commande = models.ForeignKey(
        Commande,
        on_delete=models.CASCADE,
        related_name='lignes'
    )

    produit = models.CharField(
        max_length=255
    )

    quantite = models.PositiveIntegerField()

    prix_unitaire = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    total = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    def save(self, *args, **kwargs):

        self.total = (
            self.quantite *
            self.prix_unitaire
        )

        super().save(*args, **kwargs)

    def __str__(self):

        return f"{self.produit} ({self.quantite})"