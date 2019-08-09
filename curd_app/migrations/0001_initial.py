# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-08-08 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('P_id', models.IntegerField()),
                ('P_name', models.CharField(max_length=100)),
                ('P_cost', models.IntegerField()),
                ('P_color', models.CharField(max_length=50)),
                ('P_class', models.CharField(max_length=50)),
            ],
        ),
    ]