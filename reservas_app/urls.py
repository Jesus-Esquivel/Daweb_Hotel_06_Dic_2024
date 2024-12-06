from django.urls import path
from reservas_app import views
urlpatterns = [
    path("inicio_vistaReservas",views.inicio_vistaReservas,name="inicio_vistaReservas"),
    path("registrarReservas/",views.registrarReservas,name="registarReservas"),
    path("seleccionarReservas/<id_reserva>",views.SeleccionarReservas,name="seleccionarServicios"),
    path("editarReservas/",views.editarReservas,name="editarReservas"),
    path("borrarReservas/<id_reserva>",views.borrarReservas,name="borrarReservas")
]