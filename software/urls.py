

from django.contrib import admin
from django.urls import include, path

#importando o settings e static para a vizualização de arquivos de uploads
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), #url do admin
   # path('accounts/', include('allauth.urls')), 
    path('', include('usuarios.urls')), #url do app de usuarios
    path('', include('paginas.urls')), #url do app de páginas
    path('', include('cadastros.urls')), #url do app de cadastros
    path('', include('cards.urls')), # Url do app de cards
    #path('', include('enviar_email.url')), #Envio de e-mail de "cadastro concluído com sucesso"
   
]

# Criando um if para vizualizar link url do arquivo de upload no template (em listas)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Se DEBUG = TRUE 