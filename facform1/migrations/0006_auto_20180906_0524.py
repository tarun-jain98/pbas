# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-09-06 05:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facform1', '0005_auto_20180906_0443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empdetailform',
            name='exp_indus',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='empdetailform',
            name='exp_res',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='empdetailform',
            name='exp_teach',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='empdetailform',
            name='it_f',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='empdetailform',
            name='it_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='empdetailform',
            name='it_t',
            field=models.DateField(blank=True, null=True),
        ),
    ]
