# Generated by Django 4.1.5 on 2023-02-02 10:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_dashboard'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 2, 2, 10, 44, 15, 921277, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
