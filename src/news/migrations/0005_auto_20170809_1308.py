# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 13:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20170807_1346'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-edited'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
    ]
