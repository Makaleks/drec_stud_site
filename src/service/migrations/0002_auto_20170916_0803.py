# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-16 05:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workingtime',
            name='works_to',
            field=models.TimeField(default=datetime.time(0, 0), verbose_name='Конец рабочего времени'),
        ),
    ]
