from django.db import models

class Promotion(models.Model):

    titre = models.CharField(
        max_length=255
    )

    image = models.ImageField(
        upload_to='promotions/'
    )

    description = models.TextField()

    reduction = models.PositiveIntegerField(
        default=0
    )

    active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.titre