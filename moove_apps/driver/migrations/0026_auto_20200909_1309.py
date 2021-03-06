# Generated by Django 2.2.3 on 2020-09-09 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0025_opsmetric_uber_signup'),
    ]

    operations = [
        migrations.AddField(
            model_name='opsmetric',
            name='average_earning_per_driver',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=50, null=True),
        ),
        migrations.AddField(
            model_name='opsmetric',
            name='average_fare_per_trip',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=50, null=True),
        ),
        migrations.AddField(
            model_name='opsmetric',
            name='recoveries',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
