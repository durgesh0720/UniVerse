# Generated by Django 5.0.6 on 2024-08-02 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminPannel', '0003_admin_registration_assignment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin_registration',
            name='assignment',
        ),
    ]