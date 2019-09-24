# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-12 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0005_auto_20181012_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='eps',
        ),
        migrations.AlterField(
            model_name='stock',
            name='outstanding',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='流通股本(亿)'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='totals',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='总股本(亿)'),
        ),
    ]
