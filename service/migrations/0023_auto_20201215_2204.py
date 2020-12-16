# Generated by Django 2.2.12 on 2020-12-15 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0022_remove_startupplace_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startupplace',
            name='latitude',
            field=models.FloatField(verbose_name='위도'),
        ),
        migrations.AlterField(
            model_name='startupplace',
            name='longitude',
            field=models.FloatField(verbose_name='경도'),
        ),
    ]