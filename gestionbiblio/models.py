from django.db import models

# Create your models here.
class Livre(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=100)
    anneepublication= models.IntegerField()
    genre = models.CharField(max_length=50)


    def _str_(self):
        return self.titre
    