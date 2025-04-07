from django.shortcuts import render

# Aqui irão ficar todas as views (controladores) refrente ao sistema. 
# A dunção index informa o que vai acontecer quando ela for chamada.
def index(request):
    return render(
        request, 
        'sistema/sistema.html',
        'sistema/apresentacao.html',
        
    )




# REQUEST
# RESPONSE 