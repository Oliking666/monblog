from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('panier/', views.panier, name='panier'),
    path('ajouter/<int:id>/', views.ajouter_panier, name='ajouter_panier'),
    path('commander/', views.commander, name='commander'),
]