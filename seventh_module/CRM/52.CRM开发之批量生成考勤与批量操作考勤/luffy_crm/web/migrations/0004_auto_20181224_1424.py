# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-24 06:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_userinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='user',
            new_name='name',
        ),
    ]
