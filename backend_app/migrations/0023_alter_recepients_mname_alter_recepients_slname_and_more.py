# Generated by Django 5.0.1 on 2024-04-22 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0022_recepients_account_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recepients',
            name='mname',
            field=models.CharField(default='none', max_length=255),
        ),
        migrations.AlterField(
            model_name='recepients',
            name='slname',
            field=models.CharField(default='none', max_length=255),
        ),
        migrations.AlterField(
            model_name='recepients',
            name='street2',
            field=models.CharField(default='none', max_length=255),
        ),
    ]