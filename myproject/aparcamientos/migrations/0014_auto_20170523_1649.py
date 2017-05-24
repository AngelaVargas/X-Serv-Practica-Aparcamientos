# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0013_auto_20170522_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='fondo',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='letra',
            field=models.FloatField(default=11),
        ),
    ]
