from django.db import models


class About(models.Model):

    company_name = models.CharField(max_length=200)

    presentation = models.TextField()

    history = models.TextField()

    mission = models.TextField()

    vision = models.TextField()

    values = models.TextField()

    team = models.TextField()

    image = models.ImageField(
        upload_to='about/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name