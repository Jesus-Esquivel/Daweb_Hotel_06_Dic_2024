from django.db import models

# Create your models here.
class Habitaciones(models.Model):
 id_habitaciones=models.IntegerField()
 numero_habitacion=models.CharField(max_length=50)
 tipo=models.CharField(max_length=50)
 precio_por_noche=models.CharField(max_length=100)
 Estado=models.CharField(max_length=55)

def __str__(self):
    return self.id_habitaciones
 