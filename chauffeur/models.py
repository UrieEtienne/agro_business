from about import models


class Chauffeur(models.Model):

    nom = models.CharField(max_length=255)

    telephone = models.CharField(max_length=20)

    actif = models.BooleanField(default=True)