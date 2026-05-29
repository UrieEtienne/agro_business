from django.core.mail import EmailMessage


def send_payment_receipt(paiement):

    subject = f"Paiement reçu - {paiement.reference}"

    body = f"""

    Bonjour {paiement.client_nom},

    Votre paiement de
    {paiement.montant} GNF
    a été validé avec succès.

    Référence:
    {paiement.reference}

    Merci pour votre confiance.

    Eden Agro Business

    """

    email = EmailMessage(

        subject,

        body,

        to=[paiement.email]

    )

    email.send()