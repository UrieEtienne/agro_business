from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.contrib.auth import get_user
from django.shortcuts import redirect
from django.contrib.auth.views import LogoutView


from rest_framework_simplejwt.views import (

    TokenObtainPairView,
    TokenRefreshView

)
def test_user(request):
    user = get_user(request)
    return HttpResponse(f"User: {user} | Authenticated: {user.is_authenticated}")

from django.contrib.auth import logout
from django.http import HttpResponseRedirect

def force_logout(request):
    logout(request)
    return HttpResponseRedirect("/admin/login/")

def profile_redirect(request):
    return redirect("/admin/")

urlpatterns = [
    path('admin/', admin.site.urls),

    path("test-auth/", test_user),
    path("force-logout/", force_logout),

    path('comptes/', include('comptes.urls')),

    path("accounts/profile/", profile_redirect),

    # Espace client
    path('client/', include('clients.urls')),

    # Site vitrine
    path('', include('home.urls')),
    path('about/', include('about.urls')),
    path('produits/', include('produits.urls')),
    path('gallery/', include('gallery.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('newsletter/', include('newsletter.urls')),

    # E-commerce
    path('shop/', include('ecommerce.urls')),
    path('panier/', include('panier.urls')),
    path('commandes/', include('commandes.urls')),
    path('livraisons/', include('livraisons.urls')),
    path('factures/', include('factures.urls')),
    path('paiements/', include('paiements.urls')),
    path('clients/', include('clients.urls')),
    path('stocks/', include('stocks.urls')),

    path('api/', include('clients.api_urls')),

    # JWT
    path(
        'api/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),

    path(
        'api/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )