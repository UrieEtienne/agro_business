from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

from .models import Livraison

import json


# ==============================
# LISTE DES LIVRAISONS
# ==============================

def liste_livraisons(request):

    livraisons = Livraison.objects.all().order_by(
        '-date_creation'
    )

    context = {

        'livraisons': livraisons

    }

    return render(
        request,
        'livraisons/liste_livraisons.html',
        context
    )


# ==============================
# MISE A JOUR GPS LIVRAISON
# ==============================

@csrf_exempt
def update_location(request):

    if request.method == 'POST':

        try:

            data = json.loads(request.body)

            livraison = Livraison.objects.last()

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
# ENVOI EMAIL LIVRAISON
# ==============================

def envoyer_email_livraison(livraison):

    send_mail(

        subject="Livraison confirmée",

        message=(
            "Bonjour,\n\n"
            "Votre commande est en cours de livraison.\n"
            "Merci de votre confiance.\n\n"
            "Eden Agro Business"
        ),

        from_email="edenagro@gmail.com",

        recipient_list=[
            livraison.email
        ],

        fail_silently=False
    )


# ==============================
# ENVOI WHATSAPP
# ==============================

def send_whatsapp(message, telephone):

    print(
        f"WhatsApp envoyé à {telephone} : {message}"
    )


# ==============================
# NOTIFICATION COMPLETE
# ==============================

def notifier_client_livraison(livraison):

    # EMAIL
    if livraison.email:

        envoyer_email_livraison(
            livraison
        )

    # WHATSAPP
    send_whatsapp(

        "Votre livraison est en cours.",

        livraison.telephone
    )


# ==============================
# STATISTIQUES LIVRAISONS
# ==============================

def stats(request):

    total = Livraison.objects.count()

    livrees = Livraison.objects.filter(
        statut='livree'
    ).count()

    en_cours = Livraison.objects.filter(
        statut='en_livraison'
    ).count()

    annulees = Livraison.objects.filter(
        statut='annulee'
    ).count()

    context = {

        'total': total,

        'livrees': livrees,

        'en_cours': en_cours,

        'annulees': annulees,

    }

    return render(

        request,

        'livraisons/stats.html',

        context
    )