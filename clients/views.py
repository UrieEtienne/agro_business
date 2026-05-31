from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Client
from .forms import ClientForm
from .services import historique_achats
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'clients/dashboard.html')

@login_required
def profil(request):
    return render(request, 'clients/profil.html')

@login_required
def commandes(request):
    return render(request, 'clients/commandes.html')


@login_required
def profil_client(request):

    client = Client.objects.get(
        utilisateur=request.user
    )

    achats = historique_achats(client)

    return render(

        request,

        'clients/profil_client.html',

        {

            'client': client,

            'achats': achats

        }

    )


@login_required
def modifier_profil(request):

    client = Client.objects.get(
        utilisateur=request.user
    )

    form = ClientForm(

        request.POST or None,

        request.FILES or None,

        instance=client

    )

    if form.is_valid():

        form.save()

        return redirect(
            'profil_client'
        )

    return render(

        request,

        'clients/modifier_profil.html',

        {

            'form': form

        }

    )