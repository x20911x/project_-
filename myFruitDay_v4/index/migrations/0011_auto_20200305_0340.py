# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-03-05 03:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_cartinfo_ccount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartinfo',
            name='ccount',
            field=models.IntegerField(db_column='ccount'),
        ),
    ]
