from django.db import models

class Propanflaske(models.Model):
    artikkelnummer_nykjop = models.CharField(max_length=50)
    artikkelnummer_fylling = models.TextField()
    NOBB_nykjop = models.IntegerField(default=0)
    NOBB_fylling = models.IntegerField(default=0)
    beskrivelse = models.CharField(max_length=255)
    materiale = models.CharField(max_length=255)
    ventil = models.CharField(max_length=50)
    diameter = models.IntegerField()
    hoyde = models.IntegerField()
    gassmengde = models.IntegerField()
    taravekt = models.DecimalField(max_digits=5, decimal_places=2)
    totalvekt = models.DecimalField(max_digits=5, decimal_places=2)
    bilde_id = models.IntegerField()
