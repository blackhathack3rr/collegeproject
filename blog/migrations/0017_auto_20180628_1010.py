# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-28 04:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20180628_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
