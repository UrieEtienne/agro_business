from django.db import models


class Media(models.Model):

    CATEGORY_CHOICES = (
        ('gallery', 'Galerie'),
        ('blog', 'Blog'),
    )

    TYPE_CHOICES = (
        ('image', 'Image'),
        ('video', 'Video'),
    )

    title = models.CharField(max_length=200)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    media_type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        default='image'
    )

    image = models.ImageField(
        upload_to='gallery/',
        blank=True,
        null=True
    )

    video = models.FileField(
        upload_to='videos/',
        blank=True,
        null=True
    )

    youtube_url = models.URLField(
        blank=True,
        null=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title