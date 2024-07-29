# Generated by Django 5.0.1 on 2024-07-29 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0028_temporarytransactions_accountnumber_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='temporarytransactions',
            name='city',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='temporarytransactions',
            name='country',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='temporarytransactions',
            name='email',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='temporarytransactions',
            name='fname',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='temporarytransactions',
            name='lname',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='temporarytransactions',
            name='mname',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='temporarytransactions',
            name='postal',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='temporarytransactions',
            name='region',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='temporarytransactions',
            name='slname',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='temporarytransactions',
            name='street',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='temporarytransactions',
            name='street2',
            field=models.CharField(default='', max_length=255),
        ),
    ]
