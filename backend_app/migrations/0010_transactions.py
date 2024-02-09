# Generated by Django 5.0.1 on 2024-02-09 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0009_alter_exchangerates_fee_alter_exchangerates_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moneySent', models.FloatField()),
                ('moneyReceived', models.FloatField()),
                ('currencySent', models.CharField(max_length=255)),
                ('currencyReceived', models.CharField(max_length=255)),
                ('fee', models.FloatField()),
                ('total', models.FloatField()),
                ('deliveryBank', models.CharField(max_length=255)),
                ('deliveryCash', models.CharField(max_length=255)),
                ('zenith', models.CharField(max_length=255)),
                ('gtb', models.CharField(max_length=255)),
                ('polaris', models.CharField(max_length=255)),
                ('accountNumber', models.CharField(max_length=255)),
                ('retypeAccountNumber', models.CharField(max_length=255)),
                ('checking', models.CharField(max_length=255)),
                ('savings', models.CharField(max_length=255)),
                ('fname', models.CharField(max_length=255)),
                ('mname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('slname', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('street2', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('postal', models.CharField(max_length=255)),
            ],
        ),
    ]