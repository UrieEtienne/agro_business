from django.http import JsonResponse
from .services import validate_payment


def payment_callback(request):

    reference = request.GET.get(
        'reference'
    )

    transaction_id = request.GET.get(
        'transaction_id'
    )

    paiement = validate_payment(
        reference,
        transaction_id
    )

    if paiement:

        return JsonResponse({

            'status': 'success'

        })

    return JsonResponse({

        'status': 'error'

    })