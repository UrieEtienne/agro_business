from django.shortcuts import render, get_object_or_404
from .models import Facture

from django.http import HttpResponse

from reportlab.pdfgen import canvas


def liste_factures(request):

    factures = Facture.objects.all().order_by(
        '-date_creation'
    )

    return render(
        request,
        'factures/liste_factures.html',
        {
            'factures': factures
        }
    )


def facture_pdf(request, facture_id):

    facture = get_object_or_404(
        Facture,
        id=facture_id
    )

    response = HttpResponse(
        content_type='application/pdf'
    )

    response[
        'Content-Disposition'
    ] = f'filename="facture_{facture.id}.pdf"'

    p = canvas.Canvas(response)

    p.setFont("Helvetica-Bold", 18)

    p.drawString(
        200,
        800,
        "FACTURE CLIENT"
    )

    p.setFont("Helvetica", 12)

    p.drawString(
        50,
        750,
        f"Client : {facture.client_nom}"
    )

    p.drawString(
        50,
        730,
        f"Téléphone : {facture.telephone}"
    )

    p.drawString(
        50,
        710,
        f"Adresse : {facture.adresse}"
    )

    p.drawString(
        50,
        680,
        f"Produit : {facture.produit}"
    )

    p.drawString(
        50,
        660,
        f"Quantité : {facture.quantite}"
    )

    p.drawString(
        50,
        640,
        f"Prix Unitaire : {facture.prix_unitaire} GNF"
    )

    p.drawString(
        50,
        620,
        f"TVA : {facture.tva}%"
    )

    p.drawString(
        50,
        600,
        f"Total : {facture.total()} GNF"
    )

    p.drawString(
        50,
        560,
        "Merci pour votre confiance."
    )

    p.showPage()

    p.save()

    return response