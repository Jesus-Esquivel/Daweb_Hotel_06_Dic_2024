from django.db import models

# Create your models here.
class Facturacion(models.Model):
 id_factura=models.IntegerField(primary_key=True)
 id_reserva=models.IntegerField()
 fecha_de_pago=models.DateField()
 monto_total=models.CharField(max_length=100,default='100')
 metodo_de_pago=models.CharField(max_length=50)
 
def __str__(self):
    return self.id_reserva
