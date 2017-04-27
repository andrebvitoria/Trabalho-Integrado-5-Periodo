# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0003_auto_20170417_1135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prancha',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('descricao', models.CharField(max_length=200)),
                ('altura', models.CharField(max_length=10)),
                ('litragem', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Prancha',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('descricao', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='aluguel',
            name='data_aluguel',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 17, 14, 49, 27, 547129, tzinfo=utc)),
        ),
        migrations.RemoveField(
            model_name='aluguel',
            name='prancha',
        ),
        migrations.AlterField(
            model_name='item',
            name='data_entrada',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 17, 14, 49, 27, 543631, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='prancha',
            name='tipo_prancha',
            field=models.ForeignKey(to='servicos.Tipo_Prancha'),
        ),
        migrations.AddField(
            model_name='aluguel',
            name='prancha',
            field=models.ManyToManyField(to='servicos.Prancha'),
        ),
    ]
