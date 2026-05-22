from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=250)

    image = models.ImageField(
        upload_to='blog/'
    )

    content = models.TextField()

    published = models.BooleanField(default=True)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title