# Importando o forms para personalizar formulários
from pyexpat import model
from turtle import update
from urllib import request
from django import forms
from django.contrib.auth.models import User #Classe de autenticação do django 
from django.contrib.auth.forms import UserCreationForm #, PasswordChangeForm
from django.core.exceptions import ValidationError # Método que gera um erro se os dados não corresponderem
from django.core.mail import BadHeaderError, send_mail, EmailMessage
from django.http import HttpResponse
import smtplib


#import smtplib

#from email.mime.multipart import MIMEMultipart
#from email.mime.text import MIMEText 

# Criando uma nova view e usando herança do UserCreationForm
class Usuarioform(UserCreationForm):
     #definindo o padrão de email
    email = forms.EmailField(max_length=100)

    # Classe onde conseguimos definir metadados 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] # Padrão do django
    
    #Método que evita um usuário com o mesmo email (Faz uma limpeza ou vistoria, antes do cadastro ser criado)
    def clean_email(self):
        e = self.cleaned_data['email'] #Buscando o valor do email validado
        
        # Conferindo se existe um usuário com o mesmo email com o if e else
        if User.objects.filter(email=e).exists(): # Se o email digitado for igual a 'e', email que já existe.
            raise ValidationError(f'O email {e} já existe, tente com outro!') # Retorna mensagem de erro
        else:
            return e  #Se o email não for epetido, cadastro concluído com sucesso!  
    
  
        




  


    
  



