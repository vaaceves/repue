# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-17 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20170215_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenido',
            name='slug',
            field=models.SlugField(default='textoURL-separado-por-guiones', max_length=80),
        ),
    ]
