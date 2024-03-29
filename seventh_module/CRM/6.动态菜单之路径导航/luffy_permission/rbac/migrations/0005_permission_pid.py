# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-10-12 07:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0004_auto_20181012_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='pid',
            field=models.ForeignKey(blank=True, help_text='对于非菜单权限需要选择一个可以成为菜单权的权限,用于做默认展开和选中菜单', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parents', to='rbac.Permission', verbose_name='关联权限'),
        ),
    ]
