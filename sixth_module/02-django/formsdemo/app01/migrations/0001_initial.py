# Generated by Django 2.0.1 on 2018-07-05 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('pwd', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.CharField(max_length=32)),
            ],
        ),
    ]
