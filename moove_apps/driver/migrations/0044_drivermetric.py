# Generated by Django 2.2.3 on 2020-10-26 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0043_vehicledevice'),
    ]

    operations = [
        migrations.CreateModel(
            name='DriverMetric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('driver_earnings', models.DecimalField(blank=True, decimal_places=8, max_digits=50, null=True)),
                ('cash_collected', models.DecimalField(blank=True, decimal_places=8, max_digits=50, null=True)),
                ('promotion', models.DecimalField(blank=True, decimal_places=8, max_digits=50, null=True)),
                ('tip', models.DecimalField(blank=True, decimal_places=8, max_digits=50, null=True)),
                ('total_trip_count', models.IntegerField(blank=True, null=True)),
                ('cash_trip_count', models.IntegerField(blank=True, null=True)),
                ('uber_fee_collection', models.DecimalField(blank=True, decimal_places=8, max_digits=50, null=True)),
                ('per_trip', models.DecimalField(blank=True, decimal_places=8, max_digits=50, null=True)),
                ('per_hour_online', models.DecimalField(blank=True, decimal_places=8, max_digits=50, null=True)),
                ('per_km_on_trip', models.DecimalField(blank=True, decimal_places=8, max_digits=50, null=True)),
                ('trips_per_hour', models.DecimalField(blank=True, decimal_places=8, max_digits=50, null=True)),
                ('distance_per_trip', models.DecimalField(blank=True, decimal_places=8, max_digits=50, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=8, max_digits=50, null=True)),
                ('lifetime_rating', models.DecimalField(blank=True, decimal_places=8, max_digits=50, null=True)),
                ('acceptance', models.DecimalField(blank=True, decimal_places=8, max_digits=50, null=True)),
                ('driver_cancellation_rate', models.DecimalField(blank=True, decimal_places=8, max_digits=50, null=True)),
                ('hours_online', models.TimeField(blank=True, null=True)),
                ('driver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driver.Driver')),
            ],
        ),
    ]
