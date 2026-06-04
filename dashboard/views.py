from django.shortcuts import render
from django.db.models import Sum
from django.db.models.functions import TruncDate

import json

from commandes.models import Commande
from factures.models import Facture
from panier.models import Panier
from produits.models import Produit
from .models import Stock, MouvementStock


def dashboard(request):

    # =========================
    # 📊 VENTES PAR JOUR
    # =========================
    ventes_jour = (
        Commande.objects
        .annotate(date=TruncDate("date_creation"))
        .values("date")
        .annotate(total=Sum("montant"))
        .order_by("date")
    )

    # =========================
    # 📦 KPIs
    # =========================
    total_produits = Produit.objects.count()
    total_commandes = Commande.objects.count()
    panier_actifs = Panier.objects.filter(statut="actif").count()

    factures_attente = Facture.objects.filter(statut="attente").count()
    factures_validees = Facture.objects.filter(statut="validee").count()
    factures_payees = Facture.objects.filter(statut="payee").count()

    # =========================
    # 🧾 COMMANDES RÉCENTES
    # =========================
    commandes_recentes = Commande.objects.select_related("produit").order_by("-id")[:5]

    # =========================
    # 📦 STOCKS
    # =========================
    stocks = Stock.objects.all()

    stock_labels = [s.produit.nom for s in stocks]
    stock_data = [s.quantite for s in stocks]

    # =========================
    # 🔁 MOUVEMENTS STOCK
    # =========================
    mouvements = MouvementStock.objects.all()

    mouv_labels = [m.produit.nom for m in mouvements]
    mouv_data = [m.quantite for m in mouvements]

    # =========================
    # CONTEXT FINAL UNIQUE
    # =========================
    context = {
        # KPIs
        "total_produits": total_produits,
        "total_commandes": total_commandes,
        "panier_actifs": panier_actifs,

        "factures_attente": factures_attente,
        "factures_validees": factures_validees,
        "factures_payees": factures_payees,

        # commandes
        "commandes_recentes": commandes_recentes,

        # ventes
        "ventes_jour": list(ventes_jour),

        # stocks
        "stocks": stocks,
        "stock_labels": json.dumps(stock_labels),
        "stock_data": json.dumps(stock_data),

        # mouvements
        "mouvements": mouvements,
        "mouv_labels": json.dumps(mouv_labels),
        "mouv_data": json.dumps(mouv_data),
    }

    return render(request, "dashboard.html", context)