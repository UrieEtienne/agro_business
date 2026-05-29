from django.contrib import admin
from .models import Promotion

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):

    list_display = (
        'titre',
        'reduction',
        'active',
        'created_at'
    )

    list_filter = (
        'active',
    )

    search_fields = (
        'titre',
    )