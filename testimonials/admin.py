from django.contrib import admin

from .models import Testimonial


admin.site.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'profession',
        'rating',
        'active',
        'created_at',
    )

    list_filter = (
        'active',
        'rating',
    )

    search_fields = (
        'name',
        'profession',
        'message',
    )