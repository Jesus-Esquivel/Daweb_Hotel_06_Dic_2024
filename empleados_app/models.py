from django.db import models

# Create your models here.
class Empleados(models.Model):
    id_empleados=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    telefono=models.CharField(max_length=15)
    cargo=models.CharField(max_length=50)
    fecha_de_contratacion=models.CharField(max_length=30)

    def __str__(self):
        return self.nombre