# Generated by Django 5.0.1 on 2024-01-31 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0008_exchangerates_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchangerates',
            name='fee',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='exchangerates',
            name='rate',
            field=models.IntegerField(),
        ),
    ]
