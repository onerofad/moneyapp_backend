# Generated by Django 5.0.1 on 2024-09-04 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0002_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='code',
            new_name='label',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='code1',
            new_name='value',
        ),
        migrations.RemoveField(
            model_name='country',
            name='code2',
        ),
        migrations.RemoveField(
            model_name='country',
            name='name',
        ),
        migrations.RemoveField(
            model_name='country',
            name='name1',
        ),
        migrations.RemoveField(
            model_name='country',
            name='name2',
        ),
    ]
