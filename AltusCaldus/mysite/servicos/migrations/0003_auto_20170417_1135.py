# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0002_auto_20170417_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='guarderia',
            name='cliente',
            field=models.CharField(max_length=100, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='item',
            field=models.CharField(max_length=100, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aluguel',
            name='data_aluguel',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 17, 14, 35, 14, 632264, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='item',
            name='data_entrada',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 17, 14, 35, 14, 630762, tzinfo=utc)),
        ),
    ]
