# Generated by Django 2.1.2 on 2018-10-26 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='comment_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='read_num',
            field=models.IntegerField(default=0),
        ),
    ]
