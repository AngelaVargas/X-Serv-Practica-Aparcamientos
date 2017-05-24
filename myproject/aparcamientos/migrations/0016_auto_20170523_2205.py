# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0015_auto_20170523_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='contraseña',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
