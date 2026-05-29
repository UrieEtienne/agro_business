import requests
from django.conf import settings


def generate_orange_payment(paiement):

    url = "https://api.orange.com/orange-money-webpay/dev/v1/webpayment"

    headers = {

        "Authorization":
        f"Bearer {settings.ORANGE_MONEY_API_KEY}",

        "Content-Type":
        "application/json"

    }

    payload = {

        "merchant_key":
        settings.ORANGE_MONEY_SECRET,

        "currency":
        "GNF",

        "order_id":
        paiement.reference,

        "amount":
        str(paiement.montant),

        "return_url":
        "http://127.0.0.1:8000/paiements/callback/",

        "cancel_url":
        "http://127.0.0.1:8000/paiements/cancel/",

        "notif_url":
        "http://127.0.0.1:8000/paiements/notify/"

    }

    response = requests.post(
        url,
        json=payload,
        headers=headers
    )

    return response.json()