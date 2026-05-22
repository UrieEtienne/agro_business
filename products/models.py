from django.db import models

class Product(models.Model):

    CATEGORY_CHOICES = (
        ('Fruit', 'Fruit'),
        ('Légume', 'Légume'),
        ('Céréale', 'Céréale'),
        ('Service', 'Service Agricole'),
    )

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name