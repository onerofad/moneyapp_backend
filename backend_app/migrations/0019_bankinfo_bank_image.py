# Generated by Django 5.0.1 on 2024-04-08 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0018_bankinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankinfo',
            name='bank_image',
            field=models.TextField(default=''),
        ),
    ]
