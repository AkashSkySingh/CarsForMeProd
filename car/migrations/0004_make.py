# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_auto_20170403_2202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make_display', models.CharField(max_length=200)),
                ('make_id', models.CharField(max_length=200)),
                ('make_country', models.CharField(max_length=200)),
            ],
        ),
    ]
