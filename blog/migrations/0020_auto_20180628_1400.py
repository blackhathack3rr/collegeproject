# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-28 08:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20180628_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo1',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo2',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo3',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
