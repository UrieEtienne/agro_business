from django.shortcuts import render, redirect, get_object_or_404
from .models import Panier, PanierItem
from produits.models import Produit


def get_panier(request):

    session_id = request.session.session_key

    if not session_id:

        request.session.create()

        session_id = request.session.session_key

    panier, created = Panier.objects.get_or_create(
        session_id=session_id
    )

    return panier


# AFFICHER PANIER
def panier_detail(request):

    panier = get_panier(request)

    return render(
        request,
        'panier/panier.html',
        {
            'panier': panier
        }
    )


# AJOUTER PRODUIT
def ajouter_panier(request, produit_id):

    produit = get_object_or_404(
        Produit,
        id=produit_id
    )

    panier = get_panier(request)

    item, created = PanierItem.objects.get_or_create(
        panier=panier,
        produit=produit
    )

    if not created:

        item.quantite += 1

        item.save()

    return redirect('panier_detail')


# SUPPRIMER PRODUIT
def supprimer_panier(request, item_id):

    item = get_object_or_404(
        PanierItem,
        id=item_id
    )

    item.delete()

    return redirect('panier_detail')


# DIMINUER QUANTITE
def diminuer_quantite(request, item_id):

    item = get_object_or_404(
        PanierItem,
        id=item_id
    )

    if item.quantite > 1:

        item.quantite -= 1

        item.save()

    else:

        item.delete()

    return redirect('panier_detail')

# le bouton mise en jour
def panier_view(request):

    panier_items = Panier.objects.all()

    if request.method == "POST":

        for item in panier_items:
            qte = request.POST.get(f"quantite_{item.id}")

            if qte:
                item.quantite = int(qte)
                item.save()

    total = sum(item.quantite * item.produit.prix for item in panier_items)

    return render(request, "panier.html", {
        "panier_items": panier_items,
        "total": total
    })