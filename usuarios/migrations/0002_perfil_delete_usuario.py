# Generated by Django 4.1 on 2022-09-27 22:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=50, null=True)),
                ('cpf', models.CharField(max_length=14, null=True)),
                ('telefone', models.CharField(max_length=16, null=True)),
                ('endereço', models.CharField(max_length=150, null=True)),
                ('estado', models.CharField(max_length=20, null=True)),
                ('pais', models.CharField(max_length=20, null=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]