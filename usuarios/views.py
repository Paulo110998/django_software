# CRIANDO FORMULÁRIO PARA REGISTROS DE USUÁRIO

# importando o CreateView
from ast import USub
from multiprocessing import context
from webbrowser import get
from django.views.generic.edit import CreateView, UpdateView
# Importando a classe 'User' do auth
from django.contrib.auth.models import User, Group
# Importando formulário personalizado do arquivo forms.py
from .forms import UserCreationForm, Usuarioform
# Lista os dados
from django.urls import reverse_lazy
# Importando método para buscar o grupo (objetos)
from django.shortcuts import get_object_or_404
# Importando o model de perfil do usuário
from .models import Perfil

from django.contrib.auth import views as auth_views

from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
#from django.http import HttpResponse, HttpResponseRedirect
#from django.core.mail import BadHeaderError, send_mail, EmailMessage

#from django.contrib.auth import update_session_auth_hash
#from django.contrib.auth.forms import PasswordChangeForm


# CREATEVIEW PARA CADASTRO DE USUÁRIO
class UsuarioCreate(CreateView):
    template_name = 'usuarios/registros.html' # Template html
    #classe que criará o registro
    form_class = Usuarioform
    success_url = reverse_lazy('login')
    
    # Validando o cadastro e redirecionando o usuário ao um grupo de acesso
    def  form_valid(self, form):
        #chamando o grupo
        grupo = get_object_or_404(Group, name='Funcionários')
        # Validando com o super 
        url = super().form_valid(form)
        #Adicionando o usuario/objeto ao grupo e salvando
        self.object.groups.add(grupo)
        self.object.save()
        
        # Criando um perfil para o usuário que acabou de se cadastrar
        Perfil.objects.create(usuario=self.object)

        return url

    
    # As fields já estão na classe 'Usuarioform', por isso não precisamos criálas 
    # Configurando como o título deve aparecer com o get_context_data
    def get_context_data(self, *args ,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastre-se"
        return context

    
# UPDATE 
class PerfilUpdate(UpdateView):
    template_name = 'usuarios/perfilupdate.html' 
    model = Perfil #nova classe
    fields = ['foto_perfil','nome_completo', 'cpf', 'telefone', 'endereço', 'cidade' ,'estado', 'pais']
    success_url = reverse_lazy('atualizar-dados')

    # Buscando o objeto autenticado
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil, usuario=self.request.user) 
        return self.object

    def get_context_data(self, *args ,**kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['dados'] = "Meus dados"
        context['botao'] ="Atualizar"

        return context  




    


    



        
        

    

