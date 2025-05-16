from django.urls import path
from sistema import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('listar/', views.listarUsuarios, name='listarusuarios'),
]

