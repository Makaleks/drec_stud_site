# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-24 17:44
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0010_auto_20171124_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='approved',
            field=models.BooleanField(default=True, verbose_name='Одобрено (сдана служебка)'),
        ),
        migrations.AlterField(
            model_name='service',
            name='request_document',
            field=models.FileField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'odt', 'png', 'jpg', 'jpeg'])], verbose_name='Служебка (doc/docx/pdf/odt/png/jpg/jpeg'),
        ),
        migrations.AlterField(
            model_name='service',
            name='responsible_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Ответственное лицо'),
        ),
    ]
