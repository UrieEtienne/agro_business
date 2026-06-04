from django.urls import path
from . import views

urlpatterns = [

    path('', views.liste_livraisons, name='liste_livraisons'),

    path('update-location/', views.update_location, name='update_location'),

    path('suivi/<int:id>/', views.suivi_livraison, name='suivi_livraison')
]