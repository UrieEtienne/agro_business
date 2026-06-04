from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

from .models import Livraison


@admin.register(Livraison)
class LivraisonAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'client_nom',
        'telephone',
        'ville',
        'statut_badge',
        'date_creation',
        'tracking_link',
    )

    list_filter = ('statut', 'ville')

    search_fields = ('client_nom', 'telephone', 'ville', 'code_suivi')

    ordering = ('-date_creation',)

    # =========================
    # 🗺 BOUTON TRACKING
    # =========================
    def tracking_link(self, obj):
        url = reverse('suivi_livraison', args=[obj.id])
        return format_html(
            '<a class="button" href="{}" target="_blank">🗺 Suivi</a>',
            url
        )

    tracking_link.short_description = "Tracking"

    # =========================
    # 🎯 BADGE STATUT
    # =========================
    def statut_badge(self, obj):

        colors = {
            'en_attente': 'orange',
            'en_preparation': '#6c757d',
            'expediee': '#0d6efd',
            'en_livraison': '#ffc107',
            'livree': '#198754',
            'annulee': '#dc3545',
        }

        color = colors.get(obj.statut, 'gray')

        return format_html(
            '<span style="color:white;background:{};padding:3px 8px;border-radius:5px;">{}</span>',
            color,
            obj.get_statut_display()
        )

    statut_badge.short_description = "Statut"