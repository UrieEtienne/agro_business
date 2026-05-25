from django.db import models


class Testimonial(models.Model):

    name = models.CharField(
        max_length=100
    )

    profession = models.CharField(
        max_length=150
    )

    image = models.ImageField(upload_to='testimonials/', null=True, blank=True)

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