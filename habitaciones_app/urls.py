from django.urls import path
from habitaciones_app import views
urlpatterns = [
    path("inicio_vistaHabitaciones",views.inicio_vistaHabitaciones,name="inicio_vistaHabitaciones"),
    path("registrarHabitaciones/",views.registrarHabitaciones,name="registarHabitaciones"),
    path("seleccionarHabitaciones/<id_habitaciones>",views.SeleccionarHabitaciones,name="seleccionarHabitaciones"),
    path("editarHabitaciones/",views.editarHabitaciones,name="editarHuespedes"),
    path("borrarHabitaciones/<id_habitaciones>",views.borrarHabitaciones,name="borrarHabitaciones")
]