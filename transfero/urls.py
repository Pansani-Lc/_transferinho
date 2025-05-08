from django.contrib import admin 
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sistema.urls')),
    path('usuario/', include('usuarios.urls')) , 
    path('filme/', include('filmes.urls')) , 
]






# Faltava a importação do include 

