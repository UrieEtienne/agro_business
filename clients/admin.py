from django.contrib import admin
from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):

    list_display = (

        'utilisateur',
        'telephone',
        'ville',
        'pays',
        'date_creation'

    )

    search_fields = (

        'utilisateur__username',
        'telephone',
        'ville'

    )

    list_filter = (

        'ville',
        'pays'

    )

    ordering = (

        '-date_creation',

    )