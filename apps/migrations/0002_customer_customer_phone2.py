# Generated by Django 5.0.6 on 2024-06-15 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='customer_phone2',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
