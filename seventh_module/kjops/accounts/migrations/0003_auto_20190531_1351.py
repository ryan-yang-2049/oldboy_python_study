# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-31 05:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='is_active',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='status',
            field=models.BooleanField(choices=[(1, '启用'), (2, '禁用')], default=1, verbose_name='状态'),
        ),
    ]
