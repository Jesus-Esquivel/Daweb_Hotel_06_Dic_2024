from django.shortcuts import render,redirect
from .models import Facturacion

def inicio_vistaFacturacion(request):
    lasFacturacion=Facturacion.objects.all()
    return render(request,"gestionarFacturacion.html",{"miFacturacion":lasFacturacion})


def registrarFacturacion(request):
   id_factura=request.POST["txtid_factura"]
   id_reserva=request.POST["txtid_reserva"]
   fecha_de_pago=request.POST["txtfecha_de_pago"]
   monto_total=request.POST["txtmonto_total"]
   metodo_de_pago=request.POST["txtmetodo_de_pago"] 
   
   guardarFacturacion=Facturacion.objects.create(
        id_factura=id_factura,
        id_reserva=id_reserva,
        fecha_de_pago=fecha_de_pago,
        monto_total=monto_total,
        metodo_de_pago=metodo_de_pago
   )
   return redirect("inicio_vistaFacturacion")

def SeleccionarFacturacion(request,id_factura):
    facturacion=Facturacion.objects.get(id_factura=id_factura)
    return render(request,"editarFacturacion.html",{"mifacturacion":facturacion}) 

def editarFacturacion(request):
    id_factura=request.POST["txtid_factura"]
    id_reserva=request.POST["txtid_reserva"]
    fecha_de_pago=request.POST["txtfecha_de_pago"]
    monto_total=request.POST["txtmonto_total"]
    metodo_de_pago=request.POST["txtmetodo_de_pago"]
    facturacion=Facturacion.objects.get(id_factura=id_factura)
    facturacion.id_factura=id_factura
    facturacion.id_reserva=id_reserva
    facturacion.fecha_de_pago=fecha_de_pago
    facturacion.monto_total=monto_total
    facturacion.metodo_de_pago=metodo_de_pago
    return redirect("inicio_vistaFacturacion") 

def borrarFacturacion(request,id_factura):
   facturacion=Facturacion.objects.get(id_factura=id_factura)
   facturacion.delete()
   return redirect("inicio_vistaFacturacion") 