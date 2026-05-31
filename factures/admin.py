from django.contrib import admin
from .models import Facture


@admin.register(Facture)
class FactureAdmin(admin.ModelAdmin):

    list_display = (
        'numero',
        'client_nom',
        'statut',
        'valide_par_dg',
        'valideur',
        'date_validation',
    )

    list_filter = (
        'statut',
        'valide_par_dg',
    )
    actions = ["valider_factures_par_dg"]

    def valider_factures_par_dg(self, request, queryset):

        # 🔐 SÉCURITÉ : seul superuser / DG peut valider
        if not request.user.is_superuser:
            self.message_user(
                request,
                "Accès refusé : seul le Directeur Général peut valider.",
                level="error"
            )
            return

        updated = 0

        for facture in queryset:

            # éviter double validation
            if facture.statut == "validee":
                continue

            facture.valider_par_dg(request.user)
            updated += 1

        self.message_user(
            request,
            f"{updated} facture(s) validée(s) par le DG avec succès."
        )

    valider_factures_par_dg.short_description = "Valider les factures (DG)"