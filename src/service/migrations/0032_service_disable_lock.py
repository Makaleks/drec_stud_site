# Generated by Django 2.0 on 2018-09-18 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0031_order_used'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='disable_lock',
            field=models.BooleanField(default=False, verbose_name='ОТКЛЮЧИТЬ ЗАМКИ'),
        ),
    ]