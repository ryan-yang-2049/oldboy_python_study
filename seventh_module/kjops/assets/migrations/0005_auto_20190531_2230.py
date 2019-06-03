# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-05-31 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_rentalrecord_rental_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='buy_time',
            field=models.DateField(blank=True, null=True, verbose_name='购买时间'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='价格'),
        ),
        migrations.AlterField(
            model_name='rentalrecord',
            name='rental_status',
            field=models.IntegerField(choices=[(1, '借出'), (2, '归还')], default=1, verbose_name='状态'),
        ),
    ]
