# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-26 17:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0012_auto_20171010_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='url',
            field=models.SlugField(blank=True, max_length=16, null=True, verbose_name='URL'),
        ),
    ]