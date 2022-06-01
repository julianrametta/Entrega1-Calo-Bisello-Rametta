from django.urls import path
from familia import views


urlpatterns = [
    path('familiar/', views.index_familiar, name="index_familiar"),
    path('familiar/agregar', views.agregar_familiar, name="agregar_familiar"),
    path('familiar/borrar/<identificador>', views.borrar_familiar, name="borrar_familiar"),
    path('familiar/buscar', views.buscar_familiar, name="buscar_familiar"),
    path('Vehiculos/', views.index_vehiculo, name="index_vehiculo"),
    path('Vehiculos/agregar', views.agregarVehiculo, name="agregarVehiculo"),
    path('Vehiculos/borrar/<identificador>', views.borrarVehiculo, name="borrarVehiculo"),
    path('Vehiculos/buscar', views.buscarVehiculo, name="buscarVehiculo")

]
