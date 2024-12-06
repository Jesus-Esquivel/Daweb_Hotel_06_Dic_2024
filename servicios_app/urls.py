from django.urls import path
from servicios_app import views
urlpatterns = [
    path("inicio_vistaServicios",views.inicio_vistaServicios,name="inicio_vistaServicios"),
    path("registrarServicios/",views.registrarServicios,name="registarServicios"),
    path("seleccionarServicios/<id_servicio>",views.SeleccionarServicios,name="seleccionarServicios"),
    path("editarServicios/",views.editarServicios,name="editarServicios"),
    path("borrarServicios/<id_servicio>",views.borrarServicios,name="borrarServicios")
]