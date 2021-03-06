# Generated by Django 2.2.3 on 2020-08-28 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0010_auto_20200825_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driverdailymetric',
            name='is_pos',
        ),
        migrations.RemoveField(
            model_name='driverdailymetric',
            name='total_card_amount',
        ),
        migrations.RemoveField(
            model_name='driverdailymetric',
            name='total_cash_amount',
        ),
        migrations.RemoveField(
            model_name='driverdailymetric',
            name='wait_time',
        ),
        migrations.AddField(
            model_name='driverdailymetric',
            name='cancellation_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
