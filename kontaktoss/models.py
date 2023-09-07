from django.db import models

class KontaktMelding(models.Model):
    navn = models.CharField(max_length=100)
    epost = models.EmailField()
    melding = models.TextField()

    def __str__(self):
        return self.navn
