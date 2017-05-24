# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0011_remove_aparcamiento_latitud'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aparcamiento',
            name='num',
            field=models.CharField(max_length=10),
        ),
    ]
