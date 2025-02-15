# Generated by Django 5.0.6 on 2025-01-10 13:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('task_name', models.CharField(max_length=50)),
                ('entry_date', models.DateTimeField(null=True)),
                ('entry_by', models.CharField(max_length=50, null=True)),
                ('update_date', models.DateTimeField(null=True)),
                ('update_by', models.CharField(max_length=50, null=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.room')),
            ],
        ),
    ]
