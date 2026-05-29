import qrcode

from io import BytesIO

from django.core.files import File


def generate_qr_code(facture):

    qr_data = f"""
    Facture: {facture.numero}
    Client: {facture.client_nom}
    Total: {facture.total()} GNF
    """

    qr = qrcode.make(qr_data)

    buffer = BytesIO()

    qr.save(buffer)

    filename = f'{facture.numero}.png'

    facture.qr_code.save(
        filename,
        File(buffer),
        save=False
    )