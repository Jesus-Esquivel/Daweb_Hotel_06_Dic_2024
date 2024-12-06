from django.urls import path
from facturacion_app import views
urlpatterns = [
    path("inicio_vistaFacturacion",views.inicio_vistaFacturacion,name="inicio_vistaFacturacion"),
    path("registrarFacturacion/",views.registrarFacturacion,name="registarFacturacion"),
    path("seleccionarFacturacion/<id_factura>",views.SeleccionarFacturacion,name="seleccionarFacturacion"),
    path("editarFacturacion/",views.editarFacturacion,name="editarFacturacion"),
    path("borrarFacturacion/<id_factura>",views.borrarFacturacion,name="borrarFacturacion")
]