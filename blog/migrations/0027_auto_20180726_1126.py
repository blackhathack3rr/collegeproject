# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-26 05:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_auto_20180726_1123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='majorattraction',
            new_name='attraction',
        ),
    ]