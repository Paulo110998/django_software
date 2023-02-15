# Generated by Django 4.0.5 on 2022-11-23 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0016_cadastrosempresa_jurisdicao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastromaterial',
            name='nome_material',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='cadastromaterial',
            name='tipo_material',
            field=models.CharField(max_length=50, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='cadastrosempresa',
            name='jurisdicao',
            field=models.CharField(choices=[('PJ', 'Pessoa Jurídica'), ('PF', 'Pessoa Física')], max_length=2, verbose_name='Pessoa Jurídica ou Física?'),
        ),
    ]