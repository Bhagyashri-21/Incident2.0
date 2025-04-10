# Generated by Django 5.0.6 on 2024-06-17 07:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incident_manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incident',
            name='reported_at',
        ),
        migrations.AddField(
            model_name='incident',
            name='brief_description',
            field=models.TextField(default=datetime.datetime(2024, 6, 17, 7, 39, 26, 760514, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='incident',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='attachments/'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='severity',
            field=models.CharField(max_length=50),
        ),
    ]
