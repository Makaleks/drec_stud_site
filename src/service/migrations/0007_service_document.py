# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-24 10:05
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_order_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'odt', 'png', 'jpg', 'jpeg'])], verbose_name='Служебка'),
        ),
    ]
