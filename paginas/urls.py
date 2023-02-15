
from django.urls import path, include

from .views import BemvindoView, CadastroView, IndexPaginas, LoginView, SobreView
from django.contrib.auth import views as auth_views


urlpatterns = [
     
    path('', IndexPaginas.as_view(), name='paginas'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
    path('bem-vindo/', BemvindoView.as_view(), name='bem-vindo'),
    
]



