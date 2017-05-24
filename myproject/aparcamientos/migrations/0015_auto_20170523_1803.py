# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0014_auto_20170523_1649'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='fondo',
            new_name='color',
        ),
    ]
