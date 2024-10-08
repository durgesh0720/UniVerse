# Generated by Django 5.0.6 on 2024-07-23 05:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_student_registration_id_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_registration',
            name='email',
        ),
        migrations.RemoveField(
            model_name='student_registration',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='student_registration',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='student_registration',
            name='password',
        ),
        migrations.RemoveField(
            model_name='student_registration',
            name='username',
        ),
        migrations.AddField(
            model_name='student_registration',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student_registration',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='student_registration',
            name='enrollment',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='student_registration',
            name='rollnumber',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
