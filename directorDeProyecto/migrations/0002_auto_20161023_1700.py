# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-23 22:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directorDeProyecto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='fecha_Limite',
            field=models.DateField(blank=True, null=True),
        ),
    ]
