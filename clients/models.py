from django.db import models
from django.contrib.auth.models import User
from produits.models import Produit
from django.conf import settings


# =====================================================
# CLIENT
# =====================================================



class Client(models.Model):

    utilisateur = models.OneToOneField(

        settings.AUTH_USER_MODEL,

        on_delete=models.CASCADE,

        related_name='profil_client'

    )

    photo = models.ImageField(

        upload_to='clients/',

        blank=True,

        null=True

    )

    telephone = models.CharField(
        max_length=30
    )

    adresse = models.TextField()

    ville = models.CharField(
        max_length=255
    )

    pays = models.CharField(
        max_length=255,
        default='Guinée'
    )

    date_creation = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.utilisateur.username

# =====================================================
# FAVORIS PRODUITS
# =====================================================

class Favori(models.Model):

    client = models.ForeignKey(

        Client,

        on_delete=models.CASCADE,

        related_name='favoris'

    )

    produit = models.ForeignKey(

        Produit,

        on_delete=models.CASCADE,

        related_name='favoris_clients'

    )

    date_ajout = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        unique_together = (
            'client',
            'produit'
        )

        ordering = ['-date_ajout']

    def __str__(self):

        return f"{self.client} ❤️ {self.produit}"


# =====================================================
# AVIS PRODUITS
# =====================================================

class AvisProduit(models.Model):

    NOTES = (

        (1, '1 Étoile'),

        (2, '2 Étoiles'),

        (3, '3 Étoiles'),

        (4, '4 Étoiles'),

        (5, '5 Étoiles'),

    )

    client = models.ForeignKey(

        Client,

        on_delete=models.CASCADE,

        related_name='avis'

    )

    produit = models.ForeignKey(

        Produit,

        on_delete=models.CASCADE,

        related_name='avis_clients'

    )

    note = models.IntegerField(
        choices=NOTES
    )

    commentaire = models.TextField()

    active = models.BooleanField(
        default=True
    )

    date_creation = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = ['-date_creation']

    def __str__(self):

        return f"{self.client} - {self.produit}"


# =====================================================
# WISHLIST
# =====================================================

class Wishlist(models.Model):

    client = models.OneToOneField(

        Client,

        on_delete=models.CASCADE,

        related_name='wishlist'

    )

    produits = models.ManyToManyField(

        Produit,

        blank=True

    )

    date_creation = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"Wishlist de {self.client}"


# =====================================================
# NOTIFICATIONS CLIENTS
# =====================================================

class Notification(models.Model):

    TYPES = (

        ('commande', 'Commande'),

        ('promotion', 'Promotion'),

        ('livraison', 'Livraison'),

    )

    client = models.ForeignKey(

        Client,

        on_delete=models.CASCADE,

        related_name='notifications'

    )

    titre = models.CharField(
        max_length=255
    )

    message = models.TextField()

    type_notification = models.CharField(

        max_length=50,

        choices=TYPES

    )

    lu = models.BooleanField(
        default=False
    )

    date_creation = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = ['-date_creation']

    def __str__(self):

        return self.titre


# =====================================================
# FIDELITE CLIENT
# =====================================================

class Fidelite(models.Model):

    NIVEAUX = (

        ('Bronze', 'Bronze'),

        ('Argent', 'Argent'),

        ('Or', 'Or'),

        ('Platine', 'Platine'),

    )

    client = models.OneToOneField(

        Client,

        on_delete=models.CASCADE,

        related_name='fidelite'

    )

    points = models.PositiveIntegerField(
        default=0
    )

    niveau = models.CharField(

        max_length=50,

        choices=NIVEAUX,

        default='Bronze'

    )

    def __str__(self):

        return f"{self.client} - {self.points} points"


# =====================================================
# COUPONS REDUCTION
# =====================================================

class Coupon(models.Model):

    code = models.CharField(

        max_length=50,

        unique=True

    )

    reduction = models.PositiveIntegerField(
        help_text="Pourcentage de réduction"
    )

    actif = models.BooleanField(
        default=True
    )

    date_expiration = models.DateField()

    def __str__(self):

        return self.code


# =====================================================
# SUIVI COMMANDES
# =====================================================

class SuiviCommande(models.Model):

    STATUTS = (

        ('preparee', 'Préparée'),

        ('expediee', 'Expédiée'),

        ('livree', 'Livrée'),

    )

    commande = models.ForeignKey(

        'commandes.Commande',

        on_delete=models.CASCADE,

        related_name='suivis'

    )

    statut = models.CharField(

        max_length=50,

        choices=STATUTS

    )

    localisation = models.CharField(
        max_length=255
    )

    date_update = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = ['-date_update']

    def __str__(self):

        return f"{self.commande} - {self.statut}"