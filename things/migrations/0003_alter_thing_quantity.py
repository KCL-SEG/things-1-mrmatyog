# Generated by Django 4.1.2 on 2022-10-21 17:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0002_alter_thing_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thing',
            name='quantity',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(100, 'Quantity cannot exceed 100.'), django.core.validators.MinLengthValidator(0, 'Quantity cannot be below 0.')]),
        ),
    ]
