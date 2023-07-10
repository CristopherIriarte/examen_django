from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
import django.http as http
from .forms import VideojuegoForm
from .models import Videojuego
from django.contrib.auth.decorators import login_required

def listar_videojuegos(request):
    videojuegos = Videojuego.objects.all()
    return render(request, 'juegos/listar_videojuegos.html', {'videojuegos': videojuegos})

@login_required
def crear_videojuego(request):
    if request.method == 'POST':
        form = VideojuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_videojuegos')
    else:
        form = VideojuegoForm()
    return render(request, 'juegos/crear_videojuego.html', {'form': form})

@login_required
def ver_videojuego(request, id):
    videojuego = get_object_or_404(Videojuego, id=id)
    return render(request, 'juegos/ver_videojuego.html', {'videojuego': videojuego})

@login_required
def editar_videojuego(request, id):
    videojuego = get_object_or_404(Videojuego, id=id)
    if request.method == 'POST':
        form = VideojuegoForm(request.POST, instance=videojuego)
        if form.is_valid():
            form.save()
            return redirect('listar_videojuegos')
    else:
        form = VideojuegoForm(instance=videojuego)
    return render(request, 'juegos/editar_videojuego.html', {'form': form, 'videojuego': videojuego})

@login_required
def eliminar_videojuego(request, id):
    videojuego = get_object_or_404(Videojuego, id=id)
    if request.method == 'POST':
        videojuego.delete()
        return redirect('listar_videojuegos')
    return render(request, 'juegos/eliminar_videojuego.html', {'videojuego': videojuego})

def index(request):
    return render(request, 'index.html')

def productos(request):
    return render(request, 'productos.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def venta(request):
    return render(request, 'venta.html')

def contacto(request):
    return render(request, 'contacto.html')

def api(request):
    return render(request, 'api.html')