from django.urls import path
from . import views


from .views import (

    profil_client,
    modifier_profil

)

urlpatterns = [

    path(

        'profil/',

        profil_client,

        name='profil_client'

    ),

    path(

        'modifier/',

        modifier_profil,

        name='modifier_profil'

    ),
    path('dashboard/', views.dashboard, name='client_dashboard'),
    path('profil/', views.profil, name='client_profil'),
    path('commandes/', views.commandes, name='client_commandes'),
]
