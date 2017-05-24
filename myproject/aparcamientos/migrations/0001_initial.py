# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aparcamiento',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('entidad', models.CharField(max_length=5)),
                ('nombre', models.CharField(max_length=128)),
                ('descripcion', models.TextField()),
                ('accesibilidad', models.CharField(max_length=1)),
                ('content_url', models.CharField(max_length=256)),
                ('localizacion', models.CharField(max_length=128)),
                ('clase_vial', models.CharField(max_length=128)),
                ('tipo_num', models.CharField(max_length=1)),
                ('num', models.IntegerField()),
                ('localidad', models.CharField(max_length=32)),
                ('provincia', models.CharField(max_length=32)),
                ('codigo_postal', models.IntegerField()),
                ('barrio', models.CharField(max_length=32)),
                ('distrito', models.CharField(max_length=32)),
                ('coordenada_x', models.IntegerField()),
                ('coordenada_y', models.IntegerField()),
                ('latitud', models.DecimalField(max_digits=20, decimal_places=18)),
                ('longitud', models.DecimalField(max_digits=20, decimal_places=18)),
                ('contador_coments', models.IntegerField()),
                ('telefono', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('coment', models.TextField()),
                ('aparcamiento', models.ForeignKey(to='aparcamientos.Aparcamiento')),
            ],
        ),
        migrations.CreateModel(
            name='Seleccionados',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('fecha_seleccion', models.DateField()),
                ('aparcamiento', models.ForeignKey(to='aparcamientos.Aparcamiento')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(max_length=32)),
                ('contraseña', models.CharField(max_length=32)),
                ('titulo_pagina', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='seleccionados',
            name='selector',
            field=models.ForeignKey(to='aparcamientos.Usuario'),
        ),
    ]
