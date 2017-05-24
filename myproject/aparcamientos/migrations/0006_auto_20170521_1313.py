# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0005_aparcamiento_num'),
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
    ]
