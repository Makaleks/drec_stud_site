# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-29 12:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service', '0005_auto_20170829_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='responsible_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='ответственное лицо'),
        ),
    ]