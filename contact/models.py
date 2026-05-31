from django.db import models


class Contact(models.Model):

    phone = models.CharField(max_length=100)

    whatsapp = models.CharField(max_length=100)

    email = models.EmailField()

    address = models.CharField(max_length=255)

    facebook = models.URLField(blank=True)

    instagram = models.URLField(blank=True)

    linkedin = models.URLField(blank=True)

    youtube = models.URLField(blank=True)

    google_maps = models.TextField()

    def __str__(self):
        return self.email


class ContactMessage(models.Model):

    name = models.CharField(max_length=50)

    phone = models.CharField(max_length=50)

    email = models.EmailField()

    subject = models.CharField(max_length=120)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name