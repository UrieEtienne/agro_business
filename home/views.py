from django.shortcuts import render
from gallery.models import Media
from produits.models import Produit
from blog.models import Post
from contact.models import Contact
from testimonials.models import Testimonial



# PAGE ACCUEIL
def home(request):
    testimonials = Testimonial.objects.all()
    produits = Produit.objects.all()[:6]

    posts = Post.objects.all().order_by('-created_at')[:3]

    media = Media.objects.all().order_by('-created_at')[:6]


    context = {

        'produits': produits,

        'media': media,

        'posts': posts,
        
        'testimonials': testimonials,

        'total_produits': Produit.objects.count(),

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

    total_produits = Produit.objects.count()

    total_posts = Post.objects.count()

    total_contacts = Contact.objects.count()

    context = {
        'total_media': total_media,
        'total_produits': total_produits,
        'total_posts': total_posts,
        'total_contacts': total_contacts,
    }

    return render(request, 'dashboard/dashboard.html', context)

# PAGE PUBLICITES
def publicites(request):

    return render(request, 'publicites.html')


# PAGE TEMOIGNAGES
def temoignages(request):

    testimonials = Testimonial.objects.all()

    context = {
        'testimonials': testimonials
    }

    return render(request, 'temoignages.html', context)
