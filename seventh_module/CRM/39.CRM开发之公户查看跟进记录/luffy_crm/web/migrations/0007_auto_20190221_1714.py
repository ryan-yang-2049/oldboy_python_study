# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-02-21 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_classlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classlist',
            name='tech_teachers',
            field=models.ManyToManyField(blank=True, related_name='teach_classes', to='web.UserInfo', verbose_name='任课老师'),
        ),
    ]
