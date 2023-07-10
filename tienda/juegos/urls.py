from django.urls import path
from . import views

urlpatterns = [
    path('lista', views.listar_videojuegos, name='listar_videojuegos'),
    path('crear/', views.crear_videojuego, name='crear_videojuego'),
    path('ver/<int:id>/', views.ver_videojuego, name='ver_videojuego'),
    path('editar/<int:id>/', views.editar_videojuego, name='editar_videojuego'),
    path('eliminar/<int:id>/', views.eliminar_videojuego, name='eliminar_videojuego'),
]