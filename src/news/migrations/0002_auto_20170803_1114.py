# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 11:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-edited'], 'verbose_name_plural': 'News'},
        ),
    ]
