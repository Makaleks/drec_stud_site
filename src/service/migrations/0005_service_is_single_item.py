# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-16 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_auto_20171116_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='is_single_item',
            field=models.BooleanField(default=False, verbose_name='Один предмет сервиса'),
        ),
    ]