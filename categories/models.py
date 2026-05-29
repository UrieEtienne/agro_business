from django.db import models
from django.utils.text import slugify


# =========================
# CATEGORIE
# =========================
class Categorie(models.Model):

    nom = models.CharField(
        max_length=255,
        unique=True
    )

    slug = models.SlugField(
        blank=True,
        unique=True
    )

    image = models.ImageField(
        upload_to='categories/',
        blank=True,
        null=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        verbose_name = "Catégorie"

        verbose_name_plural = "Catégories"

        ordering = ['nom']

    def save(self, *args, **kwargs):

        if not self.slug:

            self.slug = slugify(self.nom)

        super().save(*args, **kwargs)

    def __str__(self):

        return self.nom


# =========================
# SOUS CATEGORIE
# =========================
class SousCategorie(models.Model):

    categorie = models.ForeignKey(
        Categorie,
        on_delete=models.CASCADE,
        related_name='sous_categories'
    )

    nom = models.CharField(
        max_length=255
    )

    slug = models.SlugField(
        blank=True,
        unique=True
    )

    image = models.ImageField(
        upload_to='sous_categories/',
        blank=True,
        null=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        verbose_name = "Sous-catégorie"

        verbose_name_plural = "Sous-catégories"

        ordering = ['nom']

    def save(self, *args, **kwargs):

        if not self.slug:

            self.slug = slugify(self.nom)

        super().save(*args, **kwargs)

    def __str__(self):

        return f"{self.categorie.nom} → {self.nom}"