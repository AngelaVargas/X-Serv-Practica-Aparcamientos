# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0010_auto_20170522_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aparcamiento',
            name='latitud',
        ),
    ]
