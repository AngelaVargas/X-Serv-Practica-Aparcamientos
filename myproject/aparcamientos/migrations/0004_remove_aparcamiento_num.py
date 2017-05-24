# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0003_auto_20170521_1312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aparcamiento',
            name='num',
        ),
    ]
