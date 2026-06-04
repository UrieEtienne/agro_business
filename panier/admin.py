from django.contrib import admin
from .models import Panier, PanierItem


class PanierItemInline(admin.TabularInline):

    model = PanierItem

    extra = 0

@admin.register(Panier)
class PanierAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'session_id', 'created_at')
    inlines = [PanierItemInline]