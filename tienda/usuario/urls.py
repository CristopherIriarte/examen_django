from django.urls import path, include
from . import views
from .views import RegistroUsuario, UserList
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registrar', RegistroUsuario.as_view(), name="registrar"),
    path('listar', UserList.as_view(), name="list_user"),
    path('login/', LoginView.as_view(redirect_authenticated_user=True,template_name='usuario/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='usuario/logout.html'), name='logout'),
]