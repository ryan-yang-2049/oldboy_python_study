# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-06-02 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0008_auto_20190602_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='price',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='价格'),
        ),
    ]
