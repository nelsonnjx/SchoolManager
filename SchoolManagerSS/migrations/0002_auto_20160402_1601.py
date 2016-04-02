# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-02 20:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolManagerSS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='a_oUltimo',
            field=models.IntegerField(help_text='Año Donde Cursó Último Grado Aprobado', verbose_name='Año Último Grado Cursado'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='gender',
            field=models.CharField(choices=[('GM', 'Masculino'), ('GF', 'Femenino')], help_text='Genero o Sexo del Estudiante', max_length=9, verbose_name='Sexo'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='nombreMadre',
            field=models.CharField(blank=True, max_length=70, verbose_name='Nombre y Apellido de la Madre'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='nombrePadre',
            field=models.CharField(blank=True, max_length=70, verbose_name='Nombre y Apellido del Padre'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='tlfMadre',
            field=models.CharField(blank=True, max_length=12, verbose_name='Teléfono de la Madre'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='tlfPadre',
            field=models.CharField(blank=True, max_length=12, verbose_name='Teléfono del Padre'),
        ),
    ]
