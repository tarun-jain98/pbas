# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-09-04 10:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facform1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dept_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='emp_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
