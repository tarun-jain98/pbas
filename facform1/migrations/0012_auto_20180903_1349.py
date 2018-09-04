# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-09-03 13:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facform1', '0011_auto_20180902_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='empdetailform',
            name='emp_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facform1.empDetail'),
        ),
        migrations.AddField(
            model_name='feedbacktab',
            name='emp_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facform1.empDetail'),
        ),
        migrations.AddField(
            model_name='rd',
            name='emp_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facform1.empDetail'),
        ),
        migrations.AddField(
            model_name='remarks',
            name='emp_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facform1.empDetail'),
        ),
        migrations.AddField(
            model_name='remarks',
            name='hod_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='remarks',
            name='principal_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='remarks',
            name='teach_status',
            field=models.BooleanField(default=False),
        ),
    ]
