from django.shortcuts import render
from .models import Media

def gallery(request):

    medias = Media.objects.all()

    context = {
        'medias': medias
    }

    return render(request, 'gallery/gallery.html', context)