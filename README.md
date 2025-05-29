## 🎬 StreamVibe - Catálogo de Filmes e Séries

Este projeto é uma interface web para cadastro, visualização e organização de filmes e séries. Criado com foco na organização do código e clareza estrutural, a aplicação segue boas práticas de desenvolvimento utilizando Django no backend e HTML/CSS para a camada de apresentação.



##  🧩 Funcionalidades
- 🏠 Página inicial com navegação entre seções (Home, Filmes, Séries, Minha Lista).
- 🔍 Campo de busca para facilitar a navegação no catálogo.
- 🎞️ Cadastro de novos filmes com formulário seguro (CSRF protection). 
- 📄 Listagem tabular de filmes cadastrados com dados como Nome, Ano, Estúdio e Gênero.
- 📚 Rodapé organizado com links úteis e categorias.





## 📁 Estrutura do Projeto

1. **Header** (header.html) Contém: Logo com link para a página inicial. **Menu de navegação** (Home, Filmes, Séries, Minha Lista). **Campo de busca** Ícone SVG de login.

2. Formulário de Cadastro (cadastro_filmes.html) Inclui: Formulário com envio POST. Suporte a arquivos (caso necessário). Proteção CSRF e renderização automática dos campos com {{ form.as_p }}.

3. Tabela de Listagem (listar_filmes.html) Apresenta: Tabela com os dados dos filmes. Iteração do contexto filmes com exibição de ID, nome, ano, estúdio e gênero.

4. Footer (footer.html) Contém várias seções: Links relacionados à Home, Filmes, Séries e Suporte. Subcategorias como Gêneros, Lançamentos, Populares, etc.


## 📸 Aqui estão algumas imagens da interface da plataforma.
**Imagem da página incial**

![Imagem inicial](/Captura%20de%20tela%202025-05-29%20134219.png)



**Imagem da página de login** 

![Imagem login](/Captura%20de%20tela%202025-05-29%20134333.png)


**Imagem da página de cadastro** 
![Imagem cadastro](/Captura%20de%20tela%202025-05-29%20134411.png)
# Link StreamVibe 
Você pode acessar o link da plataforma por esse link 
 <http://127.0.0.1:8000/>


### 🛠️ Tecnologias Utilizadas
- Python
- Django
- HTML5
- CSS






###  📌 Organização do Código
 Agora um pouco de alguns códigos que foram usados para a formulação dessa interface
#
```python


from django.shortcuts import render , redirect  # Função para renderizar templates HTML
from  usuarios.forms import UsuarioForm



# View para exibir o formulário de login

def login(request):
    return render(
        request, 
        'usuarios/login.html'
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
            return redirect('usuario/login')      # Redireciona para a tela de login após o cadastro
        
    else:
         # Se a requisição for GET, ou seja, só para exibir a página
        form = UsuarioForm()      # Cria um formulário em branco

    return render(
        request,              # Requisição recebida
        'usuarios/cadastrar.html',       # Página HTML a ser exibida
        {'form': form}          # Envia o formulário para o template
    )

```
#
```python
from django.shortcuts import render , redirect
from sistema.models import Filme
from filmes.forms import FilmeForm


 
def cadastrarFilme(request) :
    if request.method == "POST":
     form = FilmeForm(request.POST, request.FILES)
     if form.is_valid():
      form.save()
      return redirect('listar')
    else:
        form = FilmeForm()

    return render(
        request,
        'filmes/cadastrar.html',
        {'form': form},
    )


def listarFilmes (request):
    filmes = Filme.objects.all() 


    context = {
        'filmes': filmes 
    } 

    
    
    return render (
        request, 
        'filmes/listar.html',
        context, 
    )
```






























Este projeto está dividido de forma modular:

templates/ – Contém os arquivos HTML organizados por função. static/ – Imagens e arquivos estáticos (ex: logo). views.py – Regras de exibição e controle de dados. forms.py – Formulários do Django. models.py – Estrutura dos dados de filmes/séries.


## Github
 Você pode acessar o guia do repositorio do **Github** 
<https://github.com/Pansani-Lc/_transferinho.git>

## 📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
