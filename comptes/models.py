from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    telephone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    adresse = models.TextField(
        blank=True,
        null=True
    )

    photo = models.ImageField(
        upload_to='users/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username