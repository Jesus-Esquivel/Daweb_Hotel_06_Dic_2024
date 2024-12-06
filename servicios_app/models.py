from django.db import models

# Create your models here.
class Servicios(models.Model):
 id_servicio=models.CharField(max_length=10)
 nombre=models.CharField(max_length=50)
 descripcion=models.CharField(max_length=50)
 precio=models.CharField(max_length=100)

def __str__(self):
    return self.nombre
