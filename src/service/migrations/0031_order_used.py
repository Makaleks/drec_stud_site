# Generated by Django 2.0 on 2018-09-17 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0030_auto_20180916_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='used',
            field=models.BooleanField(default=False, verbose_name='Потрачено'),
        ),
    ]
