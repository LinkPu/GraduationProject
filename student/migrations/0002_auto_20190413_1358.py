# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-13 05:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='join_time',
            field=models.DateField(auto_now_add=True, verbose_name='注册时间'),
        ),
    ]
