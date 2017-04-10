# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0009_auto_20170405_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_id', models.CharField(max_length=200, unique=True)),
                ('model_make_id', models.CharField(max_length=200)),
                ('model_name', models.CharField(max_length=200)),
                ('model_trim', models.CharField(max_length=200, unique=True)),
                ('model_year', models.CharField(max_length=200)),
                ('model_body', models.CharField(max_length=200)),
                ('model_engine_position', models.CharField(max_length=200)),
                ('model_engine_cyl', models.CharField(max_length=200)),
                ('model_engine_valves_per_cyl', models.CharField(max_length=200)),
                ('model_engine_power_rpm', models.CharField(max_length=200)),
                ('model_engine_torque_rpm', models.CharField(max_length=200)),
                ('model_engine_bore_mm', models.CharField(max_length=200)),
                ('model_engine_stroke_mm', models.CharField(max_length=200)),
                ('model_engine_compression', models.CharField(max_length=200)),
                ('model_engine_fuel', models.CharField(max_length=200)),
                ('model_top_speed_kph', models.CharField(max_length=200)),
                ('model_0_to_100_kph', models.CharField(max_length=200)),
                ('model_drive', models.CharField(max_length=200)),
                ('model_transmission_type', models.CharField(max_length=200)),
                ('model_seats', models.CharField(max_length=200)),
                ('model_doors', models.CharField(max_length=200)),
                ('model_length_mm', models.CharField(max_length=200)),
                ('model_width_mm', models.CharField(max_length=200)),
                ('model_height_mm', models.CharField(max_length=200)),
                ('model_wheelbase_mm', models.CharField(max_length=200)),
                ('model_lkm_hwy', models.CharField(max_length=200)),
                ('model_lkm_mixed', models.CharField(max_length=200)),
                ('model_lkm_city', models.CharField(max_length=200)),
                ('model_fuel_cap_l', models.CharField(max_length=200)),
                ('model_sold_in_us', models.CharField(max_length=200)),
                ('model_make_display', models.CharField(max_length=200)),
                ('make_display', models.CharField(max_length=200)),
                ('make_country', models.CharField(max_length=200)),
            ],
        ),
    ]