from django.core.mail import EmailMessage


def envoyer_facture_email(facture, pdf_file):

    email = EmailMessage(

        subject=f'Votre facture {facture.numero}',

        body='Merci pour votre achat.',

        to=[facture.client_email]

    )

    email.attach(
        f'{facture.numero}.pdf',
        pdf_file,
        'application/pdf'
    )

    email.send()