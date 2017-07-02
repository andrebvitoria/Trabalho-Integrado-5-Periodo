# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-02 01:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0002_produto_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(null=True, upload_to='static/imagem/'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='qtd',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Quantidade'),
        ),
    ]
