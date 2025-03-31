# Generated by Django 5.1.7 on 2025-03-31 19:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0002_alter_filme_sinopse_alter_usuario_cpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='imagens/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='filme',
            name='genero',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sistema.genero'),
        ),
    ]
