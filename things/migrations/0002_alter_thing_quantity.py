# Generated by Django 4.1.2 on 2022-10-21 17:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thing',
            name='quantity',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(100, 'Quantity cannot exceed 100.'), django.core.validators.MinLengthValidator(0, 'Quantity cannot be below 0.')]),
        ),
    ]