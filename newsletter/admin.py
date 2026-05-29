from django.contrib import admin
from .models import Newsletter

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):

    list_display = (
        'email',
        'active',
        'created_at'
    )

    search_fields = (
        'email',
    )

    list_filter = (
        'active',
    )