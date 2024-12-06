from django.shortcuts import render,redirect
from .models import Empleados
# Create your views here.
def inicio_vistaEmpleados(request):
    losempleados=Empleados.objects.all()
    return  render(request,"gestionarEmpleados.html",{"misempleados":losempleados})


def registrarEmpleados(request):
    id_empleados=request.POST["txtid_empleados"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"]
    email=request.POST["txtemail"]
    telefono=request.POST["txttelefono"]
    cargo=request.POST["txtcargo"]
    fecha_de_contratacion=request.POST["txtfecha_de_contratacion"]

    guardarEmpleados=Empleados.objects.create(
        id_empleados=id_empleados,
        nombre=nombre,
        apellido=apellido,
        email=email,
        telefono=telefono,
        cargo=cargo,
        fecha_de_contratacion=fecha_de_contratacion
        )    
    return redirect("inicio_vistaEmpleados")

def seleccionarEmpleados(request,id_empleados):
    empleados = Empleados.objects.get(id_empleados=id_empleados)
    return render(request,'editarEmpleados.html', {'misempleados':empleados})


def editarEmpleados(request):
    id_empleado=request.POST["txtid_empleados"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"]
    email=request.POST["txtemail"]
    telefono=request.POST["txttelefono"]
    cargo=request.POST["txtcargo"]
    fecha_de_contratacion=request.POST["txtfecha_de_contratacion"]
    empleados = Empleados.objects.get(id_empleados=id_empleado)
    empleados.nombre = nombre
    empleados.apellido = apellido
    empleados.email = email
    empleados.telefono = telefono
    empleados.cargo = cargo
    empleados.fecha_de_contratacion = fecha_de_contratacion
    empleados.save()
    return redirect("inicio_vistaEmpleados")


def borrarEmpleados(request,id_empleados):
    empleados= Empleados.objects.get(id_empleados=id_empleados)
    empleados.delete() 
    return redirect("inicio_vistaEmpleados")