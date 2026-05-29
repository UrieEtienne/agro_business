import qrcode

from io import BytesIO

from django.core.files import File


# =========================================
# GENERATION QR CODE PAIEMENT
# =========================================

def generate_payment_qr(paiement):

    data = f"""
    Paiement : {paiement.reference}

    Client : {paiement.client_nom}

    Montant : {paiement.montant} GNF
    """

    qr = qrcode.make(data)

    buffer = BytesIO()

    qr.save(buffer)

    buffer.seek(0)

    filename = f"{paiement.reference}.png"

    paiement.qr_code.save(

        filename,

        File(buffer),

        save=False

    )


# =========================================
# DETECTION FRAUDE
# =========================================

def detect_fraud(paiement):

    LIMITE_FRAUDE = 50000000

    if paiement.montant > LIMITE_FRAUDE:

        return True

    return False