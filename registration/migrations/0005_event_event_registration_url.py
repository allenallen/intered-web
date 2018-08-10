# Generated by Django 2.1 on 2018-08-08 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_registration_url',
            field=models.URLField(default='http', verbose_name='Event Registration Link'),
            preserve_default=False,
        ),
    ]
