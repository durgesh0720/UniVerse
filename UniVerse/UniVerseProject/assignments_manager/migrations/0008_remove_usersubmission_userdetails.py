# Generated by Django 5.0.6 on 2024-08-07 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignments_manager', '0007_usersubmission_userdetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersubmission',
            name='userdetails',
        ),
    ]
