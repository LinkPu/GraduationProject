# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-18 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0011_auto_20190415_2219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='activity_conndition',
            new_name='activity_condition',
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_status',
            field=models.IntegerField(choices=[(1, '已保存但未提交'), (2, '待审批'), (3, '待补充'), (4, '已通过审批'), (5, '未通过审批'), (6, '预热中'), (7, '进行中'), (8, '已结束')], default=1, verbose_name='活动状态'),
        ),
    ]
