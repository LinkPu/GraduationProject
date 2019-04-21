# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-15 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0009_auto_20190415_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='permission',
            field=models.IntegerField(choices=[(1, '公开'), (2, '私密')], verbose_name='权限'),
        ),
        migrations.AlterField(
            model_name='userfiles',
            name='relative_path',
            field=models.CharField(default='', max_length=2000, verbose_name='相对路径'),
        ),
    ]
