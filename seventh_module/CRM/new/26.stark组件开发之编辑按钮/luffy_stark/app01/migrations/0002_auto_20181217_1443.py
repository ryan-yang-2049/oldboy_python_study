# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-17 06:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='classes',
            field=models.IntegerField(choices=[(11, '全栈1期'), (21, '全栈3期')], default=11, verbose_name='班级'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='gender',
            field=models.IntegerField(choices=[(1, '男'), (2, '女')], default=1, verbose_name='性别'),
        ),
    ]
