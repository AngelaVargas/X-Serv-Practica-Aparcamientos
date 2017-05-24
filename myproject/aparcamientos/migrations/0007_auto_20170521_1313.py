# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0006_auto_20170521_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='aparcamiento',
            name='latitud',
            field=models.DecimalField(decimal_places=18, max_digits=20, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='longitud',
            field=models.DecimalField(decimal_places=18, max_digits=20, default=0),
            preserve_default=False,
        ),
    ]
