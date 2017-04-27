# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluguel',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('cliente', models.CharField(max_length=100)),
                ('prancha', models.CharField(max_length=200)),
                ('data_aluguel', models.DateTimeField(default=datetime.datetime(2017, 4, 17, 14, 27, 19, 306487, tzinfo=utc))),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='data_entrada',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 17, 14, 27, 19, 304988, tzinfo=utc)),
        ),
    ]
