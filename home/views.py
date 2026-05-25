from django.shortcuts import render
from gallery.models import Media
from products.models import Product
from blog.models import Post
from contact.models import Contact
from testimonials.models import Testimonial


# PAGE ACCUEIL
def home(request):
    testimonials = Testimonial.objects.all()
    products = Product.objects.all()[:6]

    posts = Post.objects.all().order_by('-created_at')[:3]

    media = Media.objects.all().order_by('-created_at')[:6]


    context = {

        'products': products,

        'media': media,

        'posts': posts,
        
        'testimonials': testimonials,

        'total_products': Product.objects.count(),

        'total_publications': Media.objects.count(),

        'total_articles': Post.objects.count(),

        'total_clients': Contact.objects.count(),
        'total_partenaires': 50,

        'total_experience': 10,
    }
    
    return render(request, 'home.html', context)


# DASHBOARD
def dashboard(request):

    total_media = Media.objects.count()

    total_products = Product.objects.count()

    total_posts = Post.objects.count()

    total_contacts = Contact.objects.count()

    context = {
        'total_media': total_media,
        'total_products': total_products,
        'total_posts': total_posts,
        'total_contacts': total_contacts,
    }

    return render(request, 'dashboard/dashboard.html', context)