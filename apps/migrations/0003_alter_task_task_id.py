# Generated by Django 5.0.6 on 2025-01-10 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
