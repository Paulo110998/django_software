from re import template
from django.conf.urls import include
from django.urls import path
from django.contrib.auth import views as auth_views 
from . import views

#from usuarios.forms import Redefinir
from .views import UsuarioCreate, PerfilUpdate 


urlpatterns = [
    #EX: -> path('', view, name="")
    #path('accounts/', include('allauth.urls')),
    path('login/', auth_views.LoginView.as_view(
        template_name ='usuarios/login.html'
    ), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('registrar/usuario', UsuarioCreate.as_view(), name="registrar-usuario"),
    path('atualizar/dados/usuario', PerfilUpdate.as_view(), name='atualizar-dados'),
    path('emailbemvindo/', UsuarioCreate.as_view(template_name='usuarios/email-bemvindo.html'), name='email-bemvindo'),
    
    # REDEFINIÇÃO DE SENHA DE USER
    path('reset_password', auth_views.PasswordResetView.as_view(template_name='usuarios/resetnewpassword1.html'),name='resetnewpassword'),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name='usuarios/resetnewpassword2.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='usuarios/resetnewpassword3.html'),name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='usuarios/resetnewpassword4.html'),name="password_reset_complete"),  
    #path('change-password/',auth_views.PasswordChangeView.as_view(template_name='usuarios/resetnewpassword1.html'), name= 'reset_password')
]

"""
PasswordResetView: Responsável por apresentar um formulário para que possamos preencher o e-mail de recuperação. 
Também gerará um link de uso único para a redefinição de senha e enviará esse link para o endereço de e-mail que 
for preenchido, caso o mesmo exista na base de dados.

PasswordResetDoneView: Será a página mostrada depois que o usuário recebeu o link por e-mail para redifinir a senha. 
Entenda esse método como um template que irá mostrar que o e-mail foi enviado com sucesso.

PasswordResetConfirmView: Esse método irá apresentar um formulário para inserir uma nova senha.
E esse método possui algumas caracteristicas especiais, como o argumento uidb64 e o token. O token será para identificar
se é uma senha válida conforme os padrões de segurança, já o uidb64 é o id do usuário codificado na base 64.

PasswordResetCompleteView: Responsável por exibir ao usuário um template informando que a senha foi alterada com sucesso.


"""