from django.shortcuts import render,redirect
from .models import Servicios

def inicio_vistaServicios(request):
    losservicios=Servicios.objects.all()
    return render(request,"gestionarServicios.html",{"misservicios":losservicios})


def registrarServicios(request):
    id_servicio=request.POST["txtid_servicio"]
    nombre=request.POST["txtnombre"]
    descripcion=request.POST["txtdescripcion"]
    precio=request.POST["txtprecio"]
    
    guardarServicios=Servicios.objects.create(
        id_servicio=id_servicio,
        nombre=nombre,
        descripcion=descripcion,
        precio=precio,
    )
    
    return redirect("inicio_vistaServicios")

def SeleccionarServicios(request,id_servicio):
    servicios=Servicios.objects.get(id_servicio=id_servicio)
    return render(request,"editarServicios.html",{"misservicios":servicios}) 

def editarServicios(request):
    id_servicio=request.POST["txtid_servicio"]
    nombre=request.POST["txtnombre"]
    descripcion=request.POST["txtdescripcion"]
    precio=request.POST["txtprecio"]
    servicio=Servicios.objects.get(id_servicio=id_servicio)
    servicio.id_servicio=id_servicio
    servicio.nombre=nombre
    servicio.descripcion=descripcion
    servicio.precio=precio
    return redirect("inicio_vistaServicios") 

def borrarServicios(request,id_servicio):
    servicio=Servicios.objects.get(id_servicio=id_servicio)
    servicio.delete()
    return redirect("inicio_vistaServicios") 