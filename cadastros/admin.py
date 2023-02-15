from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# 1º - Importar classes
from .models import CadastrosEmpresa, CadastroFuncionario, CadastroMaterial

# 2º - Register your models here.
admin.site.register(CadastrosEmpresa)
admin.site.register(CadastroFuncionario)
admin.site.register(CadastroMaterial)





