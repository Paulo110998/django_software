# Generated by Django 4.1 on 2022-09-27 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0010_cadastrosempresa_usuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastrofuncionario',
            name='metodo_pagamento',
            field=models.CharField(max_length=50, null=True, verbose_name='Pix'),
        ),
    ]
