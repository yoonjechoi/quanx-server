# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 21:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manseCalendar', '0002_auto_20161224_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='day',
            name='day_ground_letter',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='day',
            name='is_lunar_leap_month',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='day',
            name='is_solar_term',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='day',
            name='lunar_day',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='lunar_month',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='lunar_year',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='day',
            name='month_ground_letter',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='day',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='day',
            name='day_heaven_letter',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='day',
            name='month',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='day',
            name='month_heaven_letter',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='year',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='day',
            name='year_ground_letter',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='year_heaven_letter',
            field=models.CharField(max_length=6, null=True),
        ),
    ]