from django.shortcuts import render
from livraisons.models import Livraison

def dashboard(request):

    livraisons = Livraison.objects.filter(
        statut="en_livraison"
    )

    return render(request, "chauffeur/dashboard.html", {
        "livraisons": livraisons
    })