🎬 StreamBox - Catálogo de Filmes e Séries

Este projeto é uma interface web para cadastro, visualização e organização de filmes e séries. Criado com foco na organização do código e clareza estrutural, a aplicação segue boas práticas de desenvolvimento utilizando Django no backend e HTML/CSS para a camada de apresentação.

🧩 FUNCIONALIDADES

🏠 Página inicial com navegação entre seções (Home, Filmes, Séries, Minha Lista).
🔍 Campo de busca para facilitar a navegação no catálogo.
🎞️ Cadastro de novos filmes com formulário seguro (CSRF protection).
📄 Listagem tabular de filmes cadastrados com dados como Nome, Ano, Estúdio e Gênero.
📚 Rodapé organizado com links úteis e categorias.

📁 Estrutura do Projeto
1. Header (header.html)
Contém:
Logo com link para a página inicial.
Menu de navegação (Home, Filmes, Séries, Minha Lista).
Campo de busca.
Ícone SVG de login.

2. Formulário de Cadastro (cadastro_filmes.html)
Inclui:
Formulário com envio POST.
Suporte a arquivos (caso necessário).
Proteção CSRF e renderização automática dos campos com {{ form.as_p }}.

3. Tabela de Listagem (listar_filmes.html)
Apresenta:
Tabela com os dados dos filmes.
Iteração do contexto filmes com exibição de ID, nome, ano, estúdio e gênero.

4. Footer (footer.html)
Contém várias seções:
Links relacionados à Home, Filmes, Séries e Suporte.
Subcategorias como Gêneros, Lançamentos, Populares, etc.

🛠️ Tecnologias Utilizadas

Python 3.x
Django
HTML5
CSS3
Template engine do Django (Django Templates)
SVG (para ícones vetoriais)

📌 Organização do Código

Este projeto está dividido de forma modular:

templates/ – Contém os arquivos HTML organizados por função.
static/ – Imagens e arquivos estáticos (ex: logo).
views.py – Regras de exibição e controle de dados.
forms.py – Formulários do Django.
models.py – Estrutura dos dados de filmes/séries.

🤝 Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request com melhorias, correções ou sugestões.

📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
