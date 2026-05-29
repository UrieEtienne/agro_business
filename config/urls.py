from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


from rest_framework_simplejwt.views import (

    TokenObtainPairView,
    TokenRefreshView

)

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include('home.urls')),

    path('about/', include('about.urls')),

    path('produits/', include('produits.urls')),

    path('gallery/', include('gallery.urls')),

    path('blog/', include('blog.urls')),

    path('contact/', include('contact.urls')),
    path('newsletter/', include('newsletter.urls')),
    path('newsletter/',include('newsletter.urls')),

    # E-commerce
    path('shop/',include('ecommerce.urls')),
    path('produits/',include('produits.urls')),
    path('panier/',include('panier.urls')),
    path('commandes/',include('commandes.urls')),
    path('livraisons/',include('livraisons.urls')),
    path('factures/',include('factures.urls')),
    path('paiements/',include('paiements.urls')),
    path('clients/',include('clients.urls')),
    path('api/',include('clients.api_urls')),
    path('stocks/',include('stocks.urls')),
    path('comptes/',include('comptes.urls')),
    # Token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )