# Generated by Django 5.0.6 on 2024-07-24 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin_registration',
            fields=[
                ('id_number', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=50)),
                ('mobile', models.CharField(max_length=15, null=True)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
