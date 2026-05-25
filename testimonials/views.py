from testimonials.models import Testimonial


testimonials = Testimonial.objects.filter(
    active=True
).order_by('-created_at')