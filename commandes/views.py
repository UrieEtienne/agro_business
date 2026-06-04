from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from .models import Commande
from produits.models import Produit
from panier.models import Panier



def creer_commande(request, produit_id):

    produit = get_object_or_404(Produit, id=produit_id)

    if request.method == "POST":

        Commande.objects.create(

            produit=produit,

            nom_client=request.POST.get("nom"),

            telephone=request.POST.get("telephone"),

            adresse=request.POST.get("adresse"),

            quantite=int(request.POST.get("quantite", 1))

        )

        return redirect("home")

    return render(
        request,
        "commandes/commander.html",
        {"produit": produit}
    )

def panier_to_commande(request, panier_id):

    panier = Panier.objects.get(id=panier_id)

    commande = Commande.objects.create(
        panier=panier,
        nom_client=request.POST.get("nom"),
        telephone=request.POST.get("telephone"),
        adresse=request.POST.get("adresse"),
    )

    return redirect("facture_generer", commande.id)


def liste_commandes(request):

    commandes = Commande.objects.all().order_by('-date_creation')

    return render(
        request,
        'commandes/liste_commandes.html',
        {
            'commandes': commandes
        }
    )