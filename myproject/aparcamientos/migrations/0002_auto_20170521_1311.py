# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aparcamiento',
            name='codigo_postal',
        ),
        migrations.RemoveField(
            model_name='aparcamiento',
            name='contador_coments',
        ),
        migrations.RemoveField(
            model_name='aparcamiento',
            name='coordenada_x',
        ),
        migrations.RemoveField(
            model_name='aparcamiento',
            name='coordenada_y',
        ),
    ]
