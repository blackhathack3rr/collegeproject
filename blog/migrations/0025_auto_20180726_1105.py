# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-26 05:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20180628_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='attitude',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='besttravel',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='budget',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='carrying',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='condition',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='duration',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='hotel',
            field=models.CharField(default=django.utils.timezone.now, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='major',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
    ]
