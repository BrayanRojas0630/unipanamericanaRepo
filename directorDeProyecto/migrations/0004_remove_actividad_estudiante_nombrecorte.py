# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-27 21:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directorDeProyecto', '0003_auto_20161027_1356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actividad_estudiante',
            name='nombreCorte',
        ),
    ]
