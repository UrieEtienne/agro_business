from django.shortcuts import render
from gallery.models import Media
from products.models import Product
from blog.models import Post
from contact.models import Contact


# PAGE ACCUEIL
def home(request):

    products = Product.objects.all()[:6]

    posts = Post.objects.all().order_by('-created_at')[:3]

    media = Media.objects.all().order_by('-created_at')[:6]


    context = {
        'products': products,
        'posts': posts,
        'medias': media,
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