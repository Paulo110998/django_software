from django.views.generic import TemplateView


# Create your views here.
class IndexPaginas(TemplateView):
    template_name = 'paginas.html'

class SobreView(TemplateView):
    template_name = 'sobre.html'
#Sem uso no momento
class LoginView(TemplateView):
    template_name = 'login.html'
#Sem uso no momento
class CadastroView(TemplateView):
    template_name = 'cadastro.html'  

class BemvindoView(TemplateView):
    template_name = 'bem-vindo.html'      
