# Generated by Django 5.0.6 on 2024-08-07 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments_manager', '0009_userdetails_semester'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignmentdetails',
            name='is_checked',
        ),
        migrations.AddField(
            model_name='userdetails',
            name='is_checked',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
