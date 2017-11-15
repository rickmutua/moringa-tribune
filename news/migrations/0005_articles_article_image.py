# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 12:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20171114_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='article_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='articles/'),
            preserve_default=False,
        ),
    ]