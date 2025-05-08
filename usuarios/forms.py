from django import forms     # Importa o módulo dos formulários do django. 
from sistema.models import Usuario 

class UsuarioForm(forms.ModelForm):
    class Meta:                 # Cria um formulário baseado no model
        model = Usuario                                  # Define o model associado
        fields = ['nome','sobrenome','cpf','telefone','email','endereco','imagem', ]                        # Campos que estarão no formulário   