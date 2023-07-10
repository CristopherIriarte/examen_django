from django.db import models

class Videojuego(models.Model):
    titulo = models.CharField(max_length=100)
    consola = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=8, decimal_places=0)

    def __str__(self):
        return self.titulo
