# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_auto_20170228_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='contenido',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]