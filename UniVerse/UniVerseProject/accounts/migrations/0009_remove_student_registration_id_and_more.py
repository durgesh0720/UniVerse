# Generated by Django 5.0.6 on 2024-07-23 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_student_registration_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_registration',
            name='id',
        ),
        migrations.AddField(
            model_name='student_registration',
            name='student_id',
            field=models.IntegerField(auto_created=True, default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
