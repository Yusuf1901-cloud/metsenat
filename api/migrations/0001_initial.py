# Generated by Django 4.1.5 on 2023-01-23 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=250)),
                ('phone_num', models.CharField(max_length=13)),
                ('donate_amount', models.IntegerField()),
                ('entity_type', models.CharField(choices=[('PHY', 'PHYSICAL ENTITY'), ('LEG', 'LEGAL ENTITY')], default='PHY', max_length=3)),
                ('status', models.CharField(choices=[('NW', 'New'), ('BM', 'Being Moderated'), ('AP', 'Approved'), ('RJ', 'Rejected')], default='NW', max_length=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]