# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-23 05:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20180222_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.CharField(max_length=1000),
        ),
    ]
