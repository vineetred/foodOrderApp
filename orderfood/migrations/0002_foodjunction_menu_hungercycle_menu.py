# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderfood', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='foodjunction_menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodItem', models.CharField(max_length=300)),
                ('foodPrice', models.IntegerField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='hungercycle_menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodItem', models.CharField(max_length=300)),
                ('foodPrice', models.IntegerField(max_length=20)),
            ],
        ),
    ]
