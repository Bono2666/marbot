# Generated by Django 5.0.6 on 2025-01-11 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0012_alter_checklist_checklist_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklist',
            name='checklist_attachment',
            field=models.FileField(null=True, upload_to='checklist/'),
        ),
    ]
