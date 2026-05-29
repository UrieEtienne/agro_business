from django.urls import path

from .views import paiement_page

from .callbacks import payment_callback

urlpatterns = [

    path(
        '',
        paiement_page,
        name='paiement_page'
    ),

    path(
        'callback/',
        payment_callback,
        name='payment_callback'
    ),

]