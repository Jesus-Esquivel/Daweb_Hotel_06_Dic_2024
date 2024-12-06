from django.shortcuts import render,redirect
from .models import Huespedes

def inicio_vistaHuespedes(request):
    losHuespedes=Huespedes.objects.all()
    return render(request,"gestionarHuespedes.html",{"mishuespedes":losHuespedes})


def registrarHuespedes(request):
    id_huespedes=request.POST["txtid_huespedes"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"]
    email=request.POST["txtemail"]
    telefono=request.POST["numtelefono"]
    direccion=request.POST["txtdireccion"]
    
    guardarHuespedes=Huespedes.objects.create(
        id_huespedes=id_huespedes,
        nombre=nombre,
        apellido=apellido,
        email=email,
        telefono=telefono,
        direccion=direccion
    )
    
    return redirect("inicio_vistaHuespedes")

def SeleccionarHuespedes(request,id_huespedes):
    huespedes=Huespedes.objects.get(id_huespedes=id_huespedes)
    return render(request,"editarHuespedes.html",{"mishuespedes":huespedes}) 

def editarHuespedes(request):
    id_huespedes=request.POST["txtid_huespedes"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"]
    email=request.POST["txtemail"]
    telefono=request.POST["numtelefono"]
    direccion=request.POST["txtdireccion"]
    huespedes=Huespedes.objects.get(id_huespedes=id_huespedes)
    huespedes.id_huespedes=id_huespedes
    huespedes.nombre=nombre
    huespedes.apellido=apellido
    huespedes.email=email
    huespedes.telefono=telefono
    huespedes.direccion=direccion
    return redirect("inicio_vistaHuespedes") 

def borrarHuespedes(request,id_huespedes):
    huespedes=Huespedes.objects.get(id_huespedes=id_huespedes)
    huespedes.delete()
    return redirect("inicio_vistaHuespedes") 