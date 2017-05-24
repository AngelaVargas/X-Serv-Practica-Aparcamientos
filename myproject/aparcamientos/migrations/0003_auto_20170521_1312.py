# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0002_auto_20170521_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='aparcamiento',
            name='codigo_postal',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='contador_coments',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='coordenada_x',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='coordenada_y',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
