# Generated by Django 5.0.1 on 2024-04-10 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0019_bankinfo_bank_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='gtb',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='polaris',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='zenith',
        ),
        migrations.AddField(
            model_name='transactions',
            name='bankname',
            field=models.CharField(default='', max_length=255),
        ),
    ]
