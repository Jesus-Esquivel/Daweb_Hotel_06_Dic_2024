from django.urls import path
from empleados_app import views
urlpatterns = [
    path("inicio_vistaEmpleados",views.inicio_vistaEmpleados,name="inicio_vistaEmpleados"),
    path("registrarEmpleados/",views.registrarEmpleados,name="registarEmpleados"),
    path("seleccionarEmpleados/<id_empleados>",views.seleccionarEmpleados,name="seleccionarEmpleados"),
    path("editarEmpleados/",views.editarEmpleados,name="editarEmpleados"),
    path("borrarEmpleados/<id_empleados>",views.borrarEmpleados,name="borrarEmpleados")
]