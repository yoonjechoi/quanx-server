# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-24 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manseCalendar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField()),
                ('month', models.PositiveSmallIntegerField()),
                ('day', models.PositiveSmallIntegerField()),
                ('year_heaven_letter', models.CharField(max_length=6)),
                ('year_ground_letter', models.CharField(max_length=6)),
                ('month_heaven_letter', models.CharField(max_length=6)),
                ('day_heaven_letter', models.CharField(max_length=6)),
            ],
        ),
        migrations.DeleteModel(
            name='Time',
        ),
    ]
