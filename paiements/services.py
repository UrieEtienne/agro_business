from .models import Paiement
from .utils import detect_fraud

def validate_payment(reference, transaction_id):

    try:

        paiement = Paiement.objects.get(
            reference=reference
        )

        paiement.transaction_id = transaction_id

        paiement.statut = 'succes'

        paiement.save()

        return paiement

    except Paiement.DoesNotExist:

        return None
    
from factures.models import Facture

# FACTURE AUTOMATIQUE APRÈS PAIEMENT
def create_invoice_after_payment(paiement):

    facture = Facture.objects.create(

        client_nom=paiement.client_nom,

        telephone=paiement.telephone,

        produit='Commande E-commerce',

        quantite=1,

        prix_unitaire=paiement.montant,

        statut='payee'

    )

    return facture


# La validation du paiement

def validate_payment(reference, transaction_id):

    try:

        paiement = Paiement.objects.get(
            reference=reference
        )

        # DETECTION FRAUDE
        if detect_fraud(paiement):

            paiement.statut = 'echec'

            paiement.save()

            return None

        # VALIDATION
        paiement.transaction_id = transaction_id

        paiement.statut = 'succes'

        paiement.save()

        return paiement

    except Paiement.DoesNotExist:

        return None