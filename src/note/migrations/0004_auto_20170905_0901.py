# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-05 06:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_auto_20170905_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='name',
            field=models.SlugField(max_length=16, primary_key=True, serialize=False, verbose_name='Фрагмент URL на английском (навсегда)'),
        ),
    ]
