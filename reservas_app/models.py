from django.db import models

# Create your models here.
class Reservas(models.Model):
    id_reserva=models.CharField(max_length=10,primary_key=True)
    id_huespedes=models.CharField(max_length=10)
    id_habitacion=models.CharField(max_length=10)
    Fecha_de_Entrada=models.CharField(max_length=100)
    Fecha_de_salida=models.CharField(max_length=100)
    total_pago=models.CharField(max_length=50)
    estado=models.CharField(max_length=20)
    
def __str__(self):
        return self.id_reserva