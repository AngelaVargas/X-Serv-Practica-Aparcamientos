# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0008_auto_20170522_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='aparcamiento',
            name='latitud',
            field=models.DecimalField(max_digits=20, default=0, decimal_places=18),
        ),
    ]
