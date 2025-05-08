from django.shortcuts import render , redirect  # Função para renderizar templates HTML
from  usuarios.forms import UsuarioForm

# View para exibir o formulário de cadastro

def cadastro(request) : 
    return render(
        request,                     # Requisição HTTP recebida
        'cadastro.html'              # Template a ser renderizado
    )

# View para exibir o formulário de login

def login(request):
    return render(
        request, 
        'login.html'
    )

# Função reservada para implementar lógica de criação de usuário

def criarUsuario(request):

     # Verifica se o método da requisição é POST (envio do formulário)
    if request.method == 'POST':
         # Cria um formulário com os dados enviados (texto e imagem)
        form = UsuarioForm(request.POST, request.FILES)

         # POST: Campos de texto enviados pelo usuário
         # FILES: Arquivos enviados (como imagens)
        if form.is_valid():    # Verifica se os dados são válidos
            form.save()         # Salva o novo usuário no banco de dados
            return redirect('/usuario/login')      # Redireciona para a tela de login após o cadastro
        
    else:
         # Se a requisição for GET, ou seja, só para exibir a página
        form = UsuarioForm()      # Cria um formulário em branco

    return render(
        request,              # Requisição recebida
        'cadastro.html',       # Página HTML a ser exibida
        {'form': form}          # Envia o formulário para o template
    )