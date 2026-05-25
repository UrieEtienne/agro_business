from django.shortcuts import render
from .models import Media


def gallery(request):

    medias = Media.objects.filter(
        category='gallery',
        media_type='image'
    ).order_by('-created_at')

    context = {
        'medias': medias
    }

    return render(request, 'gallery/gallery.html', context)