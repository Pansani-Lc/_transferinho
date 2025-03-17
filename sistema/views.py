from django.shortcuts import render

# Aqui irão ficar todas as views (controladores) refrente ao sistema. 

def index(request):
    return render(
        request, 
        'sistema/index.html',
        
    )
