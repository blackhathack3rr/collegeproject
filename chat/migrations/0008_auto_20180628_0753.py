# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-28 02:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_auto_20180628_0752'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='chat',
            new_name='ChatServer',
        ),
    ]
