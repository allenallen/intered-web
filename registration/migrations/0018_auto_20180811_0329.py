# Generated by Django 2.1 on 2018-08-10 19:29

from django.db import migrations, models
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0017_auto_20180810_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_registration_url',
            field=models.URLField(blank=True, max_length=250, null=True, verbose_name='Event Registration Link'),
        ),
        migrations.AlterField(
            model_name='event',
            name='logo',
            field=s3direct.fields.S3DirectField(max_length=250),
        ),
    ]
