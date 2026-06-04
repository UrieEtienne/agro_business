from django.db import models


class Categorie(models.Model):

    nom = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)

    def __str__(self):
        return self.nom
    
class Produit(models.Model):
    nom = models.CharField(max_length=255)
    sku = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='produits/')
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    ancien_prix = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    promotion = models.BooleanField(default=False)
    description = models.TextField()
    stock = models.PositiveIntegerField(default=0)
    disponible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # ✅ IMPORTANT
    categorie = models.ForeignKey(
        Categorie,
        on_delete=models.CASCADE,
        related_name="produits"
    )

    def __str__(self):
        return self.nom