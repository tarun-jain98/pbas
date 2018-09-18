# Generated by Django 2.0.2 on 2018-09-17 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facform1', '0019_auto_20180917_0636'),
    ]

    operations = [
        migrations.AddField(
            model_name='rd',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facform1.Department'),
        ),
        migrations.AddField(
            model_name='rd',
            name='designation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facform1.Designation'),
        ),
    ]