# Generated by Django 2.0 on 2018-02-26 21:51

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0021_auto_20180226_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default=user.models.make_random_password, max_length=128, verbose_name='Хэш резервного пароля'),
        ),
    ]
