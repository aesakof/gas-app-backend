# Generated by Django 4.2.23 on 2025-06-20 17:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gas_app', '0008_fillup_fuel_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='model_year',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(2026)]),
        ),
    ]
