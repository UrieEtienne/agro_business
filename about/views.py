from django.shortcuts import render
from .models import About


def about(request):

    about_data = About.objects.first()

    context = {
        'about': about_data
    }

    return render(request, 'about/about.html', context)