# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-22 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_auto_20180621_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('place', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Add',
        ),
    ]
