# Generated by Django 2.0 on 2018-04-07 20:50

import django.core.validators
from django.db import migrations
import utils.model_aliases


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0020_question_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='image',
        ),
        migrations.AddField(
            model_name='question',
            name='attachment',
            field=utils.model_aliases.DefaultImageField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'svg'])], verbose_name='Изображение (jpg, jpeg, png, gif, svg)'),
        ),
    ]