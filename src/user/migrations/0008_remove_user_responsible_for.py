# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-29 12:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_user_responsible_for'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='responsible_for',
        ),
    ]