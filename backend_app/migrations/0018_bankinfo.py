# Generated by Django 5.0.1 on 2024-04-06 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0017_paymentmethod_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=255)),
            ],
        ),
    ]