from unicodedata import name
from webbrowser import get
from django.urls import path

from cadastros.models import CadastroMaterial, CadastroFuncionario, CadastrosEmpresa, User

# Importar as CreateViews, UpdateViews, DeleteViews e ListViews
from .views import CadastroMaterialView, CadastrosEmpresaCreate, CadastrosFuncionarioView
from .views import CadastrosEmpresaUpdate, CadastrosFuncionariosUpdate, CadastroMaterialUpdate
from .views import CadastrosEmpresaDelete, CadastrosFuncionarioDelete, CadastrosMaterialDelete
from .views import CadastrosEmpresaList, CadastrosFuncionariosList, CadastrosMaterialList
#from .views import CadastrosEmpresaListGeral, CadastrosFuncionariosListGeral, CadastrosMaterialListGeral



urlpatterns = [
    # CREATE
    #path('endereço', MinhaView.as_view(), name="name-da-url"),
    path('cadastrar/empresas/',  CadastrosEmpresaCreate.as_view() , name='cadastrar-empresas'),
    path('cadastrar/funcionarios/', CadastrosFuncionarioView.as_view(), name='cadastrar-funcionarios'),
    path('cadastrar/material/', CadastroMaterialView.as_view(), name='cadastrar-material'),
    
    #UPDATE
    path('editar/cadastros/empresas/<int:pk>/', CadastrosEmpresaUpdate.as_view(queryset=CadastrosEmpresa.objects.all()), name='editar-cadastros-empresas'),
    path('editar/cadastros/funcionarios/<int:pk>/', CadastrosFuncionariosUpdate.as_view(queryset=CadastroFuncionario.objects.all()), name='editar-cadastros-funcionarios'),
    path('editar/cadastros/material/<int:pk>/', CadastroMaterialUpdate.as_view(queryset=CadastroMaterial.objects.all()), name='editar-cadastros-material'),

    #DELETE
    path('excluir/cadastros/empresas/<int:pk>/', CadastrosEmpresaDelete.as_view(queryset=CadastrosEmpresa.objects.all()), name='excluir-cadastros-empresas'),
    path('excluir/cadastros/funcionarios/<int:pk>/', CadastrosFuncionarioDelete.as_view(queryset=CadastroFuncionario.objects.all()), name='excluir-cadastros-funcionarios'),
    path('excluir/cadastros/material/<int:pk>/', CadastrosMaterialDelete.as_view(queryset=CadastroMaterial.objects.all()), name='excluir-cadastros-material'),
    
    #LIST
    path('listar/empresas/', CadastrosEmpresaList.as_view(queryset=CadastrosEmpresa.objects.all()), name='listar-empresas'),
    path('listar/funcionarios/',  CadastrosFuncionariosList.as_view(queryset=CadastroFuncionario.objects.all()), name='listar-funcionarios'),
    path('listar/material/', CadastrosMaterialList.as_view(queryset=CadastroMaterial.objects.all()), name='listar-material'),
    

    # LISTAGEM GERAL
    #path('listar/geral/', CadastrosEmpresaListGeral.as_view(queryset=CadastrosEmpresa.objects.all()), name='listar-geral'),
    #path('listar/geral/',  CadastrosFuncionariosListGeral.as_view(queryset=CadastroFuncionario.objects.all()), name='listar-geral'),
    #path('listar/geral/', CadastrosMaterialListGeral.as_view(queryset=CadastroMaterial.objects.all()), name='listar-geral'),
]

   