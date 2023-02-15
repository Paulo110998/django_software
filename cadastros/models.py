from random import choices
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
JURISDICAO_EMPRESA = (
    ('PJ', 'Pessoa Jurídica'),
    ('PF', 'Pessoa Física'),
)

class CadastrosEmpresa(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome')
    descriçao = models.CharField(max_length=150, verbose_name='Descrição')
    jurisdicao = models.CharField(max_length=2, choices= JURISDICAO_EMPRESA, verbose_name="Pessoa Jurídica ou Física?")
    setor = models.CharField(max_length=150, verbose_name='Setor')
    documento = models.FileField(upload_to='pdf/')
    logomarca = models.ImageField(upload_to="img/",height_field=None, width_field=None, max_length=100, verbose_name='Logomarca')
    
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    

    def __str__(self):
        return f'{self.nome} | {self.descriçao}'
    


class CadastroFuncionario(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome')
    email = models.EmailField(max_length=50, verbose_name='E-mail')
    telefone = models.CharField(max_length=15, verbose_name='Telefone')
    cargo = models.CharField(max_length=20, verbose_name='Cargo', null=True)
    metodo_pagamento = models.CharField(max_length=50, verbose_name='Pix', null=True)
    data_pagamento = models.CharField(max_length=50, verbose_name='Data de Pagamento', null=True)
    valor = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    

    def __str__(self):
        return f'{self.nome} / {self.email} / {self.cargo}...'




class CadastroMaterial(models.Model):
    nome_material = models.CharField(max_length=50, verbose_name='Nome')
    tipo_material = models.CharField(max_length=50, verbose_name= 'Tipo')
    descriçao = models.CharField(max_length=150, verbose_name='Descrição')
    data_de_hoje = models.CharField(max_length=10, null=True, verbose_name='Data do cadastro')
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    
   

    def __str__(self):
        return f'{self.nome_material} / {self.tipo_material} / {self.descriçao}...'
        

