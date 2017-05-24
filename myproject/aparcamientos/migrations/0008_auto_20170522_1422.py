# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0007_auto_20170521_1313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aparcamiento',
            name='latitud',
        ),
        migrations.RemoveField(
            model_name='aparcamiento',
            name='longitud',
        ),
        migrations.AlterField(
            model_name='aparcamiento',
            name='codigo_postal',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='aparcamiento',
            name='contador_coments',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='aparcamiento',
            name='coordenada_x',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='aparcamiento',
            name='coordenada_y',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='aparcamiento',
            name='num',
            field=models.IntegerField(default=0),
        ),
    ]
