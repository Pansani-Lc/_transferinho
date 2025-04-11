from django.shortcuts import render 
from sistema.models import Filme

def listarfilmes (request):
    filme = Filme.objects.all() 


    context = {
        'filmes': filme 
    } 

    
    
    return render (
        request, 
        'filmes/listagem.html',
        context, 
    )
