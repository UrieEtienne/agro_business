from django.urls import path

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

]