# Generated by Django 4.1.5 on 2023-01-23 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_student_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sponsorship',
            options={},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['-cont_amount']},
        ),
    ]