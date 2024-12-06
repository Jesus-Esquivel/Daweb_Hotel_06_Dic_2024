from django.shortcuts import render,redirect
from .models import Reservas

def inicio_vistaReservas(request):
    lasreservas=Reservas.objects.all()
    return render(request,"gestionarReservas.html",{"misreservas":lasreservas})


def registrarReservas(request):
    id_reserva=request.POST["txtid_reserva"]
    id_huespedes=request.POST["txtid_huespedes"]
    id_habitacion=request.POST["txtid_habitacion"]
    Fecha_de_Entrada=request.POST["txtFecha_de_Entrada"]
    Fecha_de_Salida=request.POST["txtFecha_de_Salida"]
    total_pago=request.POST["numtotal_pago"]
    estado=request.POST["txtestado"]
    
    guardarReservas=Reservas.objects.create(
        id_reserva=id_reserva,
        id_huespedes=id_huespedes,
        id_habitacion=id_habitacion,
        Fecha_de_Entrada=Fecha_de_Entrada,
        Fecha_de_salida=Fecha_de_Salida,
        total_pago=total_pago,
        estado=estado
    )
    
    return redirect("inicio_vistaReservas")

def SeleccionarReservas(request,id_reserva):
    reserva=Reservas.objects.get(id_reserva=id_reserva)
    return render(request,"editarReservas.html",{"misreservas":reserva}) 

def editarReservas(request):
    id_reserva=request.POST["txtid_reserva"]
    id_huespedes=request.POST["txtid_huespedes"]
    id_habitacion=request.POST["txtid_habitacion"]
    Fecha_de_Entrada=request.POST["txtFecha_de_Entrada"]
    Fecha_de_Salida=request.POST["txtFecha_de_Salida"]
    total_pago=request.POST["numtotal_pago"]
    estado=request.POST["txtestado"]
    reserva=Reservas.objects.get(id_reserva=id_reserva)
    reserva.id_reserva=id_reserva
    reserva.id_huespedes=id_huespedes
    reserva.id_habitacion=id_habitacion
    reserva.Fecha_de_Entrada=Fecha_de_Entrada
    reserva.Fecha_de_salida=Fecha_de_Salida
    reserva.total_pago=total_pago
    reserva.estado=estado
    reserva.save()
    return redirect("inicio_vistaReservas") 

def borrarReservas(request,id_reserva):
    reserva=Reservas.objects.get(id_reserva=id_reserva)
    reserva.delete()
    return redirect("inicio_vistaReservas") 