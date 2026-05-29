from django.shortcuts import render
from testimonials.models import Testimonial


def temoignages(request):

    testimonials = Testimonial.objects.filter(
        active=True
    ).order_by('-created_at')

    return render(
        request,
        'temoignages.html',
        {
            'testimonials': testimonials
        }
    )