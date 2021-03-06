# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-22 07:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_auto_20171005_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='slug',
            field=models.SlugField(default='url-separado-por-guiones', unique=True),
        ),
        migrations.AddField(
            model_name='pais',
            name='slug',
            field=models.SlugField(default='url-separado-por-guiones', unique=True),
        ),
        migrations.AlterField(
            model_name='contenido',
            name='slug',
            field=models.SlugField(default='url-separado-por-guiones', max_length=80),
        ),
        migrations.AlterField(
            model_name='contenido',
            name='tipo',
            field=models.IntegerField(choices=[(0, 'Articulo'), (1, 'Presentaci\xf3n')], default=0),
        ),
        migrations.AlterField(
            model_name='libro',
            name='slug',
            field=models.SlugField(default='url-separado-por-guiones', unique=True),
        ),
        migrations.AlterField(
            model_name='tematica',
            name='slug',
            field=models.SlugField(default='url-separado-por-guiones', unique=True),
        ),
        migrations.DeleteModel(
            name='Clasificacion',
        ),
    ]
