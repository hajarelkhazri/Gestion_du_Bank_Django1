from django.db import models
from django.contrib.auth.models import User




class Personne(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Prenom = models.CharField(max_length=200)
    Nom = models.CharField(max_length=200)
    date_naissance = models.DateField(null=True, blank=True)
    telephone = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    ville = models.CharField(max_length=200)
    pass1=models.IntegerField(null=True)
    pass_confirm=models.IntegerField(null=True)

    def __str__(self):
        return f"{self.Prenom}"



class Compte(models.Model):
    
    proprietaire = models.OneToOneField(User, on_delete=models.CASCADE)
    compte_id=models.IntegerField(null=True)
    solde = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    def __str__(self):
        return f" {self.compte_id}"
    
class Transaction(models.Model): 

    emetteur = models.ForeignKey(Compte, related_name='transactions_emises', on_delete=models.CASCADE)
    recepteur = models.ForeignKey(Compte, related_name='transactions_recues', on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Transaction de {self.emetteur} à {self.recepteur} de {self.montant} MAD"
