# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-08 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_auto_20171102_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='account',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='Счёт'),
        ),
    ]
