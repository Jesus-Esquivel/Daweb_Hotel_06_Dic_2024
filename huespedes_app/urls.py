from django.urls import path
from huespedes_app import views
urlpatterns = [
    path("inico_vistaHuespedes",views.inicio_vistaHuespedes,name="inicio_vistaHuespedes"),
    path("registrarHuespedes/",views.registrarHuespedes,name="registarHuespedes"),
    path("seleccionarHuespedes/<id_huespedes>",views.SeleccionarHuespedes,name="seleccionarHuespedes"),
    path("editarHuespedes/",views.editarHuespedes,name="editarHuespedes"),
    path("borrarHuespedes/<id_huespedes>",views.borrarHuespedes,name="borrarHuespedes")
]