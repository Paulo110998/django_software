# 1º Importar a View
from distutils.dir_util import copy_tree
from distutils.log import Log
import email
from email.mime import image
from multiprocessing import context, get_context
from pydoc import ModuleScanner
from pyexpat import model
from webbrowser import get
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin #Controle de acesso por login de usuário
from braces.views import GroupRequiredMixin # Controle de acesso por grupos (gestão, gerência e etc)
from django.contrib.auth.models import User 
from django.shortcuts import get_object_or_404 # Configura uma página de erro mais bonita e clean


#2º Importar os models de cadastro
from .models import CadastrosEmpresa, CadastroFuncionario, CadastroMaterial

# Metódo que direciona o usuário para uma lista, após o cadastro de empresa, funcionário, material
from django.urls import reverse_lazy

# Create your views here.
############### CREATE ##################
class CadastrosEmpresaCreate(GroupRequiredMixin,LoginRequiredMixin,CreateView):
    login_url = '/login/' # Só acessa a pagina se tiver logado
    redirect_field_name = 'login' # Redireciona para o login
    group_required = u"Gestor" # Acesso restrito por grupos
    model = CadastrosEmpresa # Model
    fields = ['nome', 'descriçao', 'jurisdicao', 'setor', 'documento', 'logomarca'] # Me mostra como os campos devem aparecer
    template_name = 'cadastros/formempresa-uploads.html' # Template
    success_url = reverse_lazy('listar-empresas') # Lista os dados

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url
    
    #Método que torna possível o envio de dados para o template, através da view 
    def get_context_data(self, *args ,**kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['cadastrar'] = "Cadastrar de Cliente"
        return context


class CadastrosFuncionarioView(GroupRequiredMixin,LoginRequiredMixin,CreateView):
    login_url = '/login/' # Só acessa a pagina se tiver logado
    redirect_field_name = 'login' # Redireciona para o login
    group_required = [u"Gestor", u"Gerência"] # Acesso restrito por grupos
    model = CadastroFuncionario # Model
    fields = ['nome', 'email', 'telefone','cargo', 'metodo_pagamento', 'data_pagamento', 'valor'] # Me mostra como os campos devem aparecer
    template_name = 'cadastros/formfuncionario.html' # Template
    success_url = reverse_lazy('listar-funcionarios') # Lista os dados 

    
    #Método que valida os dados do create 
    def form_valid(self, form):

        # Antes do super não é criado o objeto nem salvo no banco
        form.instance.usuario = self.request.user 
        # form.instance -> Pegando a instância do obj no momento do cadastro
        # usuario -> coluna do model
        # self.request.user -> Buscando o usuário que fez a requisição da classe
        
        # Depois do super o objeto é criado
        url = super().form_valid(form)
        return url

    # Método que torna possível o envio de dados para o template, através da view  
    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        # Como temos o mesmo método no update, para não ficar vazio, achei por bem adicionar no create
        context['cadastrar'] = "Cadastrar Colaborador"
        return context  


class CadastroMaterialView(GroupRequiredMixin,LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'login'
    group_required = [u"Gestor", u"Gerência", u"Funcionários"]
    model = CadastroMaterial
    fields = ['id', 'nome_material', 'tipo_material', 'descriçao', 'data_de_hoje'] 
    template_name = 'cadastros/formmaterial.html'
    success_url = reverse_lazy('listar-material')  

    def  form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

    def get_context_data(self, *args ,**kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['cadastrar'] = "Cadastrar Patrimônio"
        return context    


############### UPDATE ##################
# Edita os cadastros
class CadastrosEmpresaUpdate(GroupRequiredMixin,LoginRequiredMixin, UpdateView):
    login_url = '/login/' 
    redirect_field_name = 'login' 
    group_required = u"Gestor" 
    queryset = CadastrosEmpresa.objects.all() # Me trás todos os objetos cadastrados
    models = CadastrosEmpresa 
    fields = ['nome', 'descriçao', 'setor', 'documento','logomarca'] 
    template_name = 'cadastros/formempresa.html' 
    success_url = reverse_lazy('listar-empresas') 

      # Essa comportamento é padrão, com exeção de -> "context['titulo'] = "Editar Cadastro de Empresas""
    def get_context_data(self, *args ,**kwargs):
        context = super().get_context_data(*args, **kwargs)
         
        # Dessa forma podemos alternar o título quando o usuário clicar em "editar"
        context['titulo'] = "Editar Cadastro de Clientes"
        return context
    
    
class CadastrosFuncionariosUpdate(GroupRequiredMixin,LoginRequiredMixin ,UpdateView):
    login_url = '/login/' 
    redirect_field_name = 'login' 
    group_required = [u"Gestor", u"Gerência"] 
    models = CadastroFuncionario 
    fields = ['nome', 'email', 'telefone', 'cargo', 'metodo_pagamento', 'data_pagamento', 'valor'] 
    template_name = 'cadastros/formfuncionario.html' 
    success_url = reverse_lazy('listar-funcionarios') 

    def get_object(self, queryset=None):
        # Se a pk(id) do objeto não for encontrado, retorna uma página de erro 404 mais limpa
        self.object = get_object_or_404(CadastroFuncionario, pk=self.kwargs['pk'], usuario=self.request.user)
        # Se a pk(id) do objeto não for encontrado, retorna a página de erro padrão
        #self.object = CadastroFuncionario.objects.get(pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Dados de Funcionário"
        return context    
    
     
class CadastroMaterialUpdate(GroupRequiredMixin,LoginRequiredMixin, UpdateView):
    login_url = '/login/' 
    redirect_field_name = 'login' 
    group_required = [u"Gestor", u"Gerência", u"Funcionários"] 
    models = CadastroMaterial 
    fields = ['nome_material', 'tipo_material', 'descriçao'] 
    template_name = 'cadastros/formmaterial.html' 
    success_url = reverse_lazy('listar-material') 

    def get_object(self, queryset=None):
         # Se a pk(id) do objeto não for encontrado, retorna uma página de erro 404 mais limpa
        self.object = get_object_or_404(CadastroMaterial, pk=self.kwargs['pk'], usuario=self.request.user)
        
        # Se a pk(id) do objeto não for encontrado, retorna a página de erro padrão
        #self.object = CadastroFuncionario.objects.get(pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    def get_context_data(self, *args ,**kwargs):
        context =super().get_context_data(*args, **kwargs)

        context['editar'] = "Editar Cadastro de Insumo"  
        return context  
        
################### DELETE ######################
# Excluí os cadastros
class CadastrosEmpresaDelete(GroupRequiredMixin,LoginRequiredMixin, DeleteView):
    #http_method_names = ['GET', 'POST', 'PUT', 'DELETE']
    login_url = '/login/'
    redirect_field_name = 'login'
    group_required = u"Gestor"
    models = CadastrosEmpresa
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-empresas')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['excluir_empresa'] = "Excluír Empresa:"
        return context

    
class CadastrosFuncionarioDelete(GroupRequiredMixin,LoginRequiredMixin,DeleteView):
    login_url = '/login/'
    redirect_field_name = 'login'
    group_required = [u"Gestor", u"Gerência"]
    models = CadastroFuncionario
    template_name = 'cadastros/form-excluir.html' 
    success_url = reverse_lazy('listar-funcionarios')

    def get_object(self, queryset=None):
         # Se a pk(id) do objeto não for encontrado, retorna uma página de erro 404 mais limpa
        self.object = get_object_or_404(CadastroFuncionario, pk=self.kwargs['pk'], usuario=self.request.user)
        # Se a pk(id) do objeto não for encontrado, retorna a página de erro padrão
        #self.object = CadastroFuncionario.objects.get(pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    def get_context_data(self, *args ,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['excluir_funcionario'] ="Excluír Funcionário:" 
        return context   
       

class CadastrosMaterialDelete(GroupRequiredMixin,LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'login'
    group_required = [u"Gestor", u"Gerência", u"Funcionários"]
    models = CadastroMaterial
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-material')

    def get_object(self, queryset=None):
         # Se a pk(id) do objeto não for encontrado, retorna uma página de erro 404 mais limpa
        self.object = get_object_or_404(CadastroMaterial, pk=self.kwargs['pk'], usuario=self.request.user)
        
        # Se a pk(id) do objeto não for encontrado, retorna a página de erro padrão
        #self.object = CadastroFuncionario.objects.get(pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['excluir_material'] = "Excluír Material:"  
        return context  

   
################### LIST #####################
# Lista os cadastros
class CadastrosEmpresaList(GroupRequiredMixin,LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'login'
    group_required = [u"Gestor", u"Gerência", u"Funcionários"]
    models = CadastrosEmpresa
    template_name = 'cadastros/listas/empresas.html'
    paginate_by = 9 #Paginação personalizada para facilitar a busca no banco até 10 objetos
    
    #Método de buscar de objetos do banco
    def get_queryset(self):

        # Busca do usuário, com o name do input
        buscar_empresa = self.request.GET.get('nome')
        
        # Se a busca for verdadeira, retorna o objects.filter, senão retorna todos os objetos (limpar)
        if buscar_empresa:                                    #ignora letra maiúscula + name do input
            empresas = CadastrosEmpresa.objects.filter(nome__icontains=buscar_empresa) 
        else:
            empresas = CadastrosEmpresa.objects.all()    

        return empresas

     


class CadastrosFuncionariosList(GroupRequiredMixin,LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'login'
    group_required = [u"Gestor", u"Gerência", u"Funcionários"]
    model = CadastroFuncionario
    template_name = 'cadastros/listas/funcionarios.html' 
    paginate_by = 9 # Paginação personalizada para facilitar a busca no banco
     
    # Método que por padrão lista todos os objetos criados
    def get_queryset(self):
        #self.object_list = CadastroFuncionario.objects.all() #-> Padrão
        self.object_list = CadastroFuncionario.objects.filter(usuario=self.request.user)#-> Listando apenas os objetos criados pelo o usuário logado
        return self.object_list

    def get_queryset(self):

        buscar_funcionarios = self.request.GET.get('nome')    

        if buscar_funcionarios:
            funcionarios = CadastroFuncionario.objects.filter(nome__icontains=buscar_funcionarios)
        else:
            funcionarios = CadastroFuncionario.objects.all()

        return funcionarios        



class CadastrosMaterialList(GroupRequiredMixin,LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'login'
    group_required = [u"Gestor", u"Gerência", u"Funcionários"]
    models = CadastroMaterial
    template_name = 'cadastros/listas/material.html' 
    paginate_by = 9
    

    # Método que por padrão lista todos os objetos criados
    def get_queryset(self):
        #object_list = CadastroFuncionario.objects.all() #-> Padrão
        self.object_list=CadastroMaterial.objects.filter(usuario=self.request.user)
        return self.object_list


    def get_queryset(self):

        buscar_material = self.request.GET.get('nome_material')    

        if buscar_material:
            material = CadastroMaterial.objects.filter(nome_material__icontains=buscar_material)
        else:
            material = CadastroMaterial.objects.all()

        return material   

        



