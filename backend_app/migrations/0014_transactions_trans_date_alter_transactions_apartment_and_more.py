# Generated by Django 5.0.1 on 2024-02-19 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0013_alter_transactions_checking_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='trans_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='apartment',
            field=models.CharField(default='none', max_length=255),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='mname',
            field=models.CharField(default='none', max_length=255),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='nickname',
            field=models.CharField(default='none', max_length=255),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='slname',
            field=models.CharField(default='none', max_length=255),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='street2',
            field=models.CharField(default='none', max_length=255),
        ),
    ]
