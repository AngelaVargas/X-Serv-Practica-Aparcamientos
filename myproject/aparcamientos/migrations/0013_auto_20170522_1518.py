# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0012_auto_20170522_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aparcamiento',
            name='codigo_postal',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='aparcamiento',
            name='coordenada_x',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='aparcamiento',
            name='coordenada_y',
            field=models.CharField(max_length=32),
        ),
    ]
