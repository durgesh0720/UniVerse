# Generated by Django 5.0.6 on 2024-08-10 20:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_manager', '0002_alter_attendanceyear_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancemonth',
            name='month',
            field=models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)]),
        ),
    ]