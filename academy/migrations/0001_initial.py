# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-13 05:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=60, verbose_name='名称')),
                ('school_num', models.CharField(max_length=20, null=True, verbose_name='院校账号')),
                ('school_pwd', models.CharField(max_length=200, null=True, verbose_name='院校密码')),
                ('school_tel', models.CharField(max_length=15, null=True, verbose_name='院校电话')),
                ('status', models.IntegerField(choices=[(1, '使用中'), (2, '停用'), (3, '未开通')], default=3, verbose_name='院校状态')),
            ],
            options={
                'db_table': 'academy',
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('code_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='编号')),
                ('parent_id', models.IntegerField(verbose_name='父级编号')),
                ('area_name', models.CharField(max_length=180, verbose_name='区域名称')),
            ],
            options={
                'db_table': 'area',
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major_name', models.CharField(max_length=100, verbose_name='专业名称')),
            ],
            options={
                'db_table': 'major',
            },
        ),
        migrations.AddField(
            model_name='academy',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.Area', verbose_name='城市id'),
        ),
        migrations.AddField(
            model_name='academy',
            name='major',
            field=models.ManyToManyField(to='academy.Major', verbose_name='院校专业'),
        ),
    ]
