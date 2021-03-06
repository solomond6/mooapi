# Generated by Django 2.2.3 on 2020-09-07 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0020_auto_20200902_1109'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpsMetric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('driver_appointment', models.IntegerField(blank=True, null=True)),
                ('driver_assessment', models.IntegerField(blank=True, null=True)),
                ('driver_approved', models.IntegerField(blank=True, null=True)),
                ('driver_serving_time', models.TimeField(blank=True, null=True)),
                ('driver_waiting_time', models.TimeField(blank=True, null=True)),
                ('driver_approval_to_car_time', models.TimeField(blank=True, null=True)),
                ('driver_showroom_footfall', models.IntegerField(blank=True, null=True)),
                ('uber_showroom_footfall', models.IntegerField(blank=True, null=True)),
                ('non_uber_showroom_footfall', models.IntegerField(blank=True, null=True)),
                ('verification_submissions', models.IntegerField(blank=True, null=True)),
                ('driver_submissions', models.IntegerField(blank=True, null=True)),
                ('guarantor_submissions', models.IntegerField(blank=True, null=True)),
                ('driver_verification', models.IntegerField(blank=True, null=True)),
                ('guarantor_verification', models.IntegerField(blank=True, null=True)),
                ('number_verified', models.IntegerField(blank=True, null=True)),
                ('guarantor_failed_verification', models.IntegerField(blank=True, null=True)),
                ('driver_failed_verification', models.IntegerField(blank=True, null=True)),
                ('driver_flexi_rentals', models.IntegerField(blank=True, null=True)),
                ('driver_income_products', models.IntegerField(blank=True, null=True)),
                ('driver_stop_gap', models.IntegerField(blank=True, null=True)),
                ('assigned_drivers', models.IntegerField(blank=True, null=True)),
                ('active_drivers', models.IntegerField(blank=True, null=True)),
                ('active_vehicles', models.IntegerField(blank=True, null=True)),
                ('uber_qualified_incentives', models.IntegerField(blank=True, null=True)),
                ('supply_hours', models.IntegerField(blank=True, null=True)),
                ('supply_hours_to_drivers', models.IntegerField(blank=True, null=True)),
                ('trips_completed', models.IntegerField(blank=True, null=True)),
                ('flexi_trips', models.IntegerField(blank=True, null=True)),
                ('income_trips', models.IntegerField(blank=True, null=True)),
                ('trips_completed_to_supply_hour', models.IntegerField(blank=True, null=True)),
                ('gross_bookings', models.DecimalField(blank=True, decimal_places=8, max_digits=50, null=True)),
                ('net_earnings', models.DecimalField(blank=True, decimal_places=8, max_digits=50, null=True)),
                ('cash_trips', models.IntegerField(blank=True, null=True)),
                ('card_trips', models.IntegerField(blank=True, null=True)),
                ('p_non_cash_trip', models.DecimalField(blank=True, decimal_places=8, max_digits=50, null=True)),
                ('virtual_account_trip', models.IntegerField(blank=True, null=True)),
                ('p_virtual_account_trip', models.DecimalField(blank=True, decimal_places=8, max_digits=50, null=True)),
                ('cars_with_pos', models.IntegerField(blank=True, null=True)),
                ('pos_transaction', models.IntegerField(blank=True, null=True)),
                ('p_pos_transaction', models.DecimalField(blank=True, decimal_places=8, max_digits=50, null=True)),
                ('distance_travelled', models.DecimalField(blank=True, decimal_places=8, max_digits=50, null=True)),
                ('trip_distance', models.DecimalField(blank=True, decimal_places=8, max_digits=50, null=True)),
                ('p_ontrip_distance', models.DecimalField(blank=True, decimal_places=8, max_digits=50, null=True)),
                ('uber_deactivation', models.IntegerField(blank=True, null=True)),
                ('apprehension', models.IntegerField(blank=True, null=True)),
                ('minor_accident', models.IntegerField(blank=True, null=True)),
                ('major_accident', models.IntegerField(blank=True, null=True)),
                ('accidents', models.IntegerField(blank=True, null=True)),
                ('returns', models.IntegerField(blank=True, null=True)),
                ('Vehicle_first_trip', models.IntegerField(blank=True, null=True)),
                ('roadworthy_vehicle', models.IntegerField(blank=True, null=True)),
                ('vehicle_signup', models.IntegerField(blank=True, null=True)),
                ('vehicle_maintained', models.IntegerField(blank=True, null=True)),
                ('assigned_vehicle', models.IntegerField(blank=True, null=True)),
                ('vehicle_inspection_due', models.IntegerField(blank=True, null=True)),
                ('vehicle_inspection_completed', models.IntegerField(blank=True, null=True)),
                ('vehicle_inspection_outstanding', models.IntegerField(blank=True, null=True)),
                ('vehicle_collection', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
