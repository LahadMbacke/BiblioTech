from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Livre(models.Model):
    titre  = models.CharField(max_length=100)
    auteur = models.CharField(max_length=100)
    categorie = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    disponibilite = models.BooleanField(default=True)

    def __str__(self):
        return self.titre



class Emprunt(models.Model):
    livre  = models.ForeignKey(Livre, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_emprunt = models.DateTimeField(auto_now_add=True)
    date_retour = models.DateTimeField()

    def __str__(self):
        return self.livre.titre + ' - ' + self.user.username