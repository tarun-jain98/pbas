# Generated by Django 2.0.2 on 2018-09-17 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facform1', '0017_auto_20180917_0510'),
    ]

    operations = [
        migrations.AddField(
            model_name='rd',
            name='doc_link',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
