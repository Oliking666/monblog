from django.db import models

# Create your models here.
class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='produits/')

    def __str__(self):
        return self.nom

class Commande(models.Model):
    nom_client = models.CharField(max_length=100)
    email = models.EmailField()
    produits = models.ManyToManyField(Produit)
    date_commande = models.DateTimeField(auto_now_add=True)

