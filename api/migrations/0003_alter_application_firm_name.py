# Generated by Django 4.1.5 on 2023-01-23 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_application_firm_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='firm_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
