"""
Django settings for nodate project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
from telnetlib import LOGOUT


import os
# Build paths inside the project like this: BASE_DIR / 'subdir'. -> Construindo caminhos dentro do projeto
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@w()#&v-&#!&lytzl5%pz43vo=hb6)kp-of89sl6b!smy&%xhi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True #Permite que a página de erro retorne para o dev

ALLOWED_HOSTS = []


# Application definition - Instalação de apps

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'paginas.apps.PaginasConfig',
    'cadastros.apps.CadastrosConfig',
    'usuarios.apps.UsuariosConfig',
    'cards.apps.CardsConfig',
    'crispy_forms',
    #Aplicativo que permite excluir arquivos antigos automaticamente, ao editar arquivos de uploads.
    'django_cleanup.apps.CleanupConfig',
    
]



CRISPY_TEMPLATE_PACK = 'bootstrap4' # Definindo a biblioteca

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nodate.urls' # Projeto Gerado

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # Definindo o name padrão
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'nodate.wsgi.application'


# Database (Conexão)
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nodate',
        'USER': 'root',
        'PASSWORD':'', 
        'HOST': '127.0.0.1', 
        'PORT': '3306', 
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'pt-br' #alterado para pt-br (Portugûes do Brasil)

TIME_ZONE = 'America/Sao_Paulo' # Alterado

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# Static -> Permite que meu projeto busque sempre a pasta 'static(img, css, js)'
STATIC_URL = 'static/'

STATICFILES_DIRS= [
    os.path.join(BASE_DIR, 'static'),
]

# ARQUIVOS DE MEDIA/UPLOAD

#Direcionando os uploads para uma pasta do projeto chamada "uploads"
MEDIA_ROOT = os.path.join(BASE_DIR, "uploads")
MEDIA_URL = '/uploads/' # Constante que possibilita a vizualização do arquivo


#obs: Caso for hospedar seu projeto em algum site de hospedagem
# leia "media_root" na documentação do django.




# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# CONFIGURAÇÃO DE AUTENTICAÇÃO (Login/Logout) -> Controle de entrada e saída do usuário

LOGIN_REDIRECT_URL = 'bem-vindo' # Após o login, redireciona para o 'bem-vindo'

LOGIN_URL = "login" # Redireciona para a url de login

LOGOUT_REDIRECT = "login" # Após o logout, redireciona para a página de login.



# REDEFINIÇÃO DE SENHA (Configurações para envio de e-mail)

# S M T P -> Simple Mail Transfer Protocol (Protocolo de envio de e-mail simples).
#Mime -> É uma norma de envio de mensagens pela internet, padrão de envio de mensagem códificado.

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 

# Conexão com o servidor do gmail
DEFAULT_FROM_EMAIL = 'Vox Communications'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = "587"
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'testes.djangoframe@gmail.com'
EMAIL_HOST_PASSWORD = "yhxkbvfujatnenaz"

server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)





