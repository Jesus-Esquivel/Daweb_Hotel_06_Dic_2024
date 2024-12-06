from django.shortcuts import render,redirect
from .models import Habitaciones
def inicio_vistaHabitaciones(request):
    lasHabitaciones=Habitaciones.objects.all()
    return render(request,"gestionarHabitaciones.html",{"mishabitaciones":lasHabitaciones})


def registrarHabitaciones(request):
    id_habitaciones=request.POST["txtid_habitaciones"]
    numero_habitacion=request.POST["txtnumero_habitacion"]
    tipo=request.POST["txttipo"]
    precio_por_noche=request.POST["txtprecio_por_noche"]
    Estado=request.POST["txtEstado"]
    
    guardarHabitaciones=Habitaciones.objects.create(
        id_habitaciones=id_habitaciones,
        numero_habitacion=numero_habitacion,
        tipo=tipo,
        precio_por_noche=precio_por_noche,
        Estado=Estado
    )
    
    return redirect("inicio_vistaHabitaciones")

def SeleccionarHabitaciones(request,id_habitaciones):
    habitaciones=Habitaciones.objects.get(id_habitaciones=id_habitaciones)
    return render(request,"editarHabitaciones.html",{"misHabitaciones":habitaciones}) 

def editarHabitaciones(request):
    id_habitaciones=request.POST["txtid_habitaciones"]
    numero_habitaciones=request.POST["txtnumero_habitacion"]
    tipo=request.POST["txttipo"]
    precio_por_noche=request.POST["txtprecio_por_noche"]
    habitaciones=Habitaciones.objects.get(id_habitaciones=id_habitaciones)
    habitaciones.id_habitaciones=id_habitaciones
    habitaciones.numero_habitacion=numero_habitaciones
    habitaciones.tipo=tipo
    habitaciones.precio_por_noche=precio_por_noche
    return redirect("inicio_vistaHabitaciones") 

def borrarHabitaciones(request,id_habitaciones):
    habitaciones=Habitaciones.objects.get(id_habitaciones=id_habitaciones)
    habitaciones.delete()
    return redirect("inicio_vistaHabitaciones") 