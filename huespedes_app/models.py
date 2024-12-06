from django.db import models

# Create your models here.
class Huespedes(models.Model):
   id_huespedes=models.CharField (max_length=10,primary_key=True)
   nombre=models.CharField(max_length=100)
   apellido=models.CharField(max_length=100)
   email=models.CharField(max_length=40)
   telefono=models.CharField(max_length=15)
   direccion=models.CharField(max_length=50)
   
def __str__(self):
   return self.id_huespedes