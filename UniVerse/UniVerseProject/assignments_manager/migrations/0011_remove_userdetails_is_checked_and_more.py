# Generated by Django 5.0.6 on 2024-08-07 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments_manager', '0010_remove_assignmentdetails_is_checked_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='is_checked',
        ),
        migrations.AddField(
            model_name='usersubmission',
            name='is_checked',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
