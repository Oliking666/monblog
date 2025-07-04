from django.shortcuts import render, redirect
from .models import Produit, Commande


def accueil(request):
    produits = Produit.objects.all()
    return render(request, 'accueil.html', {'produits': produits})


def ajouter_panier(request, id):
    panier = request.session.get('panier', [])
    if id not in panier:
        panier.append(id)
    request.session['panier'] = panier
    return redirect('accueil')


def panier(request):
    ids = request.session.get('panier', [])
    produits = Produit.objects.filter(id__in=ids)
    return render(request, 'panier.html', {'produits': produits})


def commander(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        ids = request.session.get('panier', [])
        if ids:
            commande = Commande.objects.create(nom_client=nom, email=email)
            for pid in ids:
                produit = Produit.objects.get(id=pid)
                commande.produits.add(produit)
            commande.save()
            request.session['panier'] = []
            return render(request, 'merci.html')
    return redirect('panier')
# Create your views here.
