# Generated by Django 4.1 on 2022-09-23 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0006_cadastrosempresa_documento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastrosempresa',
            name='logo_cliente',
            field=models.ImageField(default=1, height_field=150, upload_to='img/', verbose_name='Logomarca', width_field=150),
            preserve_default=False,
        ),
    ]
