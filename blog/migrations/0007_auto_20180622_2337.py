# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-22 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=200),
        ),
    ]
