# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-23 18:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciclo',
            fields=[
                ('nombre', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('nombre', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('nombre', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('codigo_programa', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('idFacultad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiante.Facultad')),
            ],
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('nombre', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='facultad',
            name='idSede',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiante.Sede'),
        ),
    ]