# Generated by Django 5.0.1 on 2024-10-23 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0012_temporarytransactions_trans_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=255)),
                ('user_handle', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('entity_name', models.CharField(max_length=255)),
                ('identity_value', models.CharField(max_length=255)),
                ('identity_alias', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('address_alias', models.CharField(max_length=255)),
                ('street_address_1', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=255)),
                ('crypto_address', models.CharField(max_length=255)),
                ('crypto_alias', models.CharField(max_length=255)),
                ('birthdate', models.CharField(max_length=255)),
                ('session_identifier', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='temporarytransactions',
            name='trans_id',
            field=models.CharField(default=2260134454, max_length=255),
        ),
    ]
