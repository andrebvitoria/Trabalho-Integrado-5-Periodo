# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-21 15:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DetalheAluguel',
            new_name='ItemAluguel',
        ),
        migrations.RenameModel(
            old_name='DetalheAula',
            new_name='ItemAula',
        ),
        migrations.RenameModel(
            old_name='DetalheGuarderia',
            new_name='ItemGuarderia',
        ),
    ]
