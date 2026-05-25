from django.db import models


class Testimonial(models.Model):

    MEDIA_CHOICES = (
        ('image', 'Image'),
        ('video', 'Video'),
    )

    name = models.CharField(
        max_length=100
    )

    profession = models.CharField(
        max_length=150
    )

    media_type = models.CharField(
        max_length=10,
        choices=MEDIA_CHOICES,
        default='image'
    )

    image = models.ImageField(
        upload_to='testimonials/',
        null=True,
        blank=True
    )

    video = models.FileField(
        upload_to='testimonials/videos/',
        null=True,
        blank=True
    )

    youtube_url = models.URLField(
        blank=True,
        null=True
    )

    message = models.TextField()

    rating = models.IntegerField(
        default=5
    )

    active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name