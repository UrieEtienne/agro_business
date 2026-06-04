from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core.exceptions import ValidationError
from commandes.models import Commande
import uuid
from decimal import Decimal


class Facture(models.Model):

    STATUTS = [
        ('en_attente', 'En attente'),
        ('validee', 'Validée DG'),
        ('payee', 'Payée'),
    ]

    # =========================
    # LIEN COMMANDE
    # =========================
    commande = models.ForeignKey(
        Commande,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    # =========================
    # STATUT
    # =========================
    statut = models.CharField(
        max_length=20,
        choices=STATUTS,
        default='en_attente'
    )

    # =========================
    # ENTREPRISE
    # =========================
    entreprise_nom = models.CharField(max_length=255, default="Eden Agro Business")
    entreprise_adresse = models.TextField(default="Conakry - Guinée")
    entreprise_telephone = models.CharField(max_length=30, default="+224 XXX XX XX XX")
    entreprise_email = models.EmailField(default="contact@edenagro.com")
    entreprise_site = models.URLField(blank=True, null=True)
    entreprise_logo = models.ImageField(upload_to='entreprise/logo/', blank=True, null=True)
    entreprise_rccm = models.CharField(max_length=100, blank=True, null=True)
    entreprise_nif = models.CharField(max_length=100, blank=True, null=True)

    # =========================
    # FACTURE
    # =========================
    numero = models.CharField(max_length=50, unique=True, blank=True)

    client_nom = models.CharField(max_length=255)
    client_email = models.EmailField()
    telephone = models.CharField(max_length=30)
    adresse = models.TextField()

    produit = models.CharField(max_length=255)
    quantite = models.PositiveIntegerField()

    prix_unitaire = models.DecimalField(max_digits=12, decimal_places=2)

    tva = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal("18.00"))

    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    commentaire_validation = models.TextField(blank=True, null=True)

    # =========================
    # VALIDATION DG
    # =========================
    valide_par_dg = models.BooleanField(default=False)

    date_validation = models.DateTimeField(null=True, blank=True)

    valideur = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='factures_validees'
    )

    # =========================
    # DATES
    # =========================
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    # =========================
    # SAVE
    # =========================
    def save(self, *args, **kwargs):

        if not self.numero:
            annee = timezone.now().year
            uid = uuid.uuid4().hex[:6].upper()
            self.numero = f"FAC-{annee}-{uid}"

        # validation automatique cohérente
        if self.valide_par_dg and self.statut == "en_attente":
            self.statut = "validee"
            if not self.date_validation:
                self.date_validation = timezone.now()

        super().save(*args, **kwargs)

    # =========================
    # LOGIQUE
    # =========================
    def est_validable(self):
        return self.statut == "en_attente"

    def valider_par_dg(self, user):
        if self.statut != "en_attente":
            raise ValidationError("Facture déjà validée ou payée.")

        self.valide_par_dg = True
        self.valideur = user
        self.statut = "validee"
        self.date_validation = timezone.now()
        self.save()

    # =========================
    # CALCULS
    # =========================
    def sous_total(self):
        return self.quantite * self.prix_unitaire

    def montant_tva(self):
        return (self.sous_total() * self.tva) / Decimal("100")

    def total(self):
        return self.sous_total() + self.montant_tva()

    # =========================
    # VALIDATION DJANGO
    # =========================
    def clean(self):
        if self.statut == 'payee' and not self.valide_par_dg:
            raise ValidationError(
                "Le Directeur Général doit valider la facture avant paiement."
            )

    # =========================
    # STRING
    # =========================
    def __str__(self):
        return f"{self.numero} - {self.client_nom}"