# Generated by Django 2.2.3 on 2020-09-07 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0023_auto_20200907_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='opsmetric',
            name='driver_first_trip',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='opsmetric',
            name='non_cash_trip',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
