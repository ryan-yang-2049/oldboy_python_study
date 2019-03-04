# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-03-01 03:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='pid',
            field=models.ForeignKey(blank=True, help_text='对于一个部门,可以选择一个上级部门', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parents', to='asset.Department', verbose_name='关联部门'),
        ),
    ]