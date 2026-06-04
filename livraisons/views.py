from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from .models import Livraison  
import json
from .utils import get_lat_lng


# ==============================
# création ou modification livraison
# ==============================
def create_livraison(request):

    livraison = Livraison(
        client_nom="Ali",
        telephone="622xxxx",
        adresse="Kaloum",
        ville="Conakry"
    )

    # 🔥 AUTO GPS ICI
    lat, lng = get_lat_lng(livraison.adresse, livraison.ville)

    livraison.latitude = lat
    livraison.longitude = lng

    livraison.save()

# ==============================
# LISTE DES LIVRAISONS
# ==============================

def liste_livraisons(request):

    livraisons_list = Livraison.objects.all().order_by('-date_creation')

    return render(request, 'livraisons/liste_livraisons.html', {
        'livraisons': livraisons_list
    })


# ==============================
# MISE A JOUR GPS LIVRAISON
# ==============================

@csrf_exempt
def update_location(request):

    if request.method == 'POST':

        try:
            data = json.loads(request.body)

            livraison = Livraison.objects.last()  # ✅ correction

            if livraison:

                livraison.latitude = data.get('lat')
                livraison.longitude = data.get('lng')
                livraison.save()

                return JsonResponse({
                    "status": "success",
                    "message": "Position mise à jour"
                })

            return JsonResponse({
                "status": "error",
                "message": "Aucune livraison trouvée"
            })

        except Exception as e:
            return JsonResponse({
                "status": "error",
                "message": str(e)
            })

    return JsonResponse({
        "status": "error",
        "message": "Méthode non autorisée"
    })


# ==============================
# ENVOI EMAIL
# ==============================

def envoyer_email_livraison(livraison):

    send_mail(
        subject="Livraison confirmée",
        message="Votre commande est en cours de livraison.",
        from_email="edenagro@gmail.com",
        recipient_list=[livraison.email],
        fail_silently=False
    )


# ==============================
# NOTIFICATION
# ==============================

def notifier_client_livraison(livraison):

    if livraison.email:
        envoyer_email_livraison(livraison)


# ==============================
# STATISTIQUES
# ==============================

def stats(request):

    total = Livraison.objects.count()
    livrees = Livraison.objects.filter(statut='livree').count()
    en_cours = Livraison.objects.filter(statut='en_livraison').count()
    annulees = Livraison.objects.filter(statut='annulee').count()

    return render(request, 'livraisons/stats.html', {
        'total': total,
        'livrees': livrees,
        'en_cours': en_cours,
        'annulees': annulees,
    })


# ==============================
# SUIVI LIVRAISON
# ==============================

def suivi_livraison(request, id):
    livraison = get_object_or_404(Livraison, id=id)

    return render(request, "livraisons/suivi.html", {
        "livraison": livraison
    })


# ==============================
# IA ESTIMATION
# ==============================

def estimation_livraison(distance_km):

    if distance_km < 5:
        return "15 - 30 min"
    elif distance_km < 15:
        return "30 - 60 min"
    else:
        return "1 - 2 heures"