from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# portfolio/views.py

def home(request):
    return render(request, 'home.html')

def home(request):
    return HttpResponse("Bienvenue sur la page d’accueil du portfolio")

def contact(request):
    return HttpResponse("Voici la page de contact")
