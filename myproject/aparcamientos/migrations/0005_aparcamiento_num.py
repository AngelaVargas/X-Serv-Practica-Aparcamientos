# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0004_remove_aparcamiento_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='aparcamiento',
            name='num',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
