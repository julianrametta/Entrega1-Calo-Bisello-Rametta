from django.urls import path
from familia import views


urlpatterns = [
    path('familiar/', views.index_familiar, name="index_familiar"),
    path('familiar/agregar', views.agregar_familiar, name="agregar_familiar"),
    path('familiar/borrar/<identificador>', views.borrar_familiar, name="borrar_familiar"),
    path('familiar/buscar', views.buscar_familiar, name="buscar_familiar"),
    path('mascota/', views.index_mascota, name="index_mascota"),
    path('mascota/agregar', views.agregar_mascota, name="agregar_mascota"),
    path('mascota/borrar/<identificador>', views.borrar_mascota, name="borrar_mascota"),
    path('mascota/buscar', views.buscar_mascota, name="buscar_mascota"),
]
