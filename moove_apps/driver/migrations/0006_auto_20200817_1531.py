# Generated by Django 2.2.3 on 2020-08-17 15:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0005_auto_20200815_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='vehicle',
        ),
        migrations.CreateModel(
            name='PosSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos_terminal_id', models.CharField(max_length=100)),
                ('effective_start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('effective_end_date', models.DateTimeField(blank=True, null=True)),
                ('vehicle', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pos', to='driver.Vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='DriverVehicleAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effective_start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('effective_end_date', models.DateTimeField(blank=True, null=True)),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assingment', to='driver.Driver')),
                ('vehicle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assingment', to='driver.Vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='DriverDailyMetric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('total_earned', models.DecimalField(decimal_places=6, default=0.0, max_digits=8)),
                ('net_earnings', models.DecimalField(decimal_places=6, default=0.0, max_digits=8)),
                ('trips', models.IntegerField()),
                ('fare', models.DecimalField(decimal_places=6, default=0.0, max_digits=8)),
                ('wait_time', models.TimeField()),
                ('toll', models.IntegerField()),
                ('uber_fee', models.DecimalField(decimal_places=6, default=0.0, max_digits=8)),
                ('cash_collected', models.DecimalField(decimal_places=6, default=0.0, max_digits=8)),
                ('tips', models.CharField(blank=True, max_length=100, null=True)),
                ('cancellation', models.IntegerField()),
                ('adjusted_fare', models.DecimalField(decimal_places=6, default=0.0, max_digits=8)),
                ('surge', models.DecimalField(decimal_places=6, default=0.0, max_digits=8)),
                ('airport_surcharge', models.DecimalField(decimal_places=6, default=0.0, max_digits=8)),
                ('total_card_amount', models.DecimalField(decimal_places=6, default=0.0, max_digits=8)),
                ('total_cash_amount', models.DecimalField(decimal_places=6, default=0.0, max_digits=8)),
                ('cash_payment_count', models.IntegerField(default=0)),
                ('card_payment_count', models.IntegerField(default=0)),
                ('duration_online', models.TimeField()),
                ('rating', models.DecimalField(decimal_places=6, default=0.0, max_digits=8)),
                ('acceptance_rate', models.DecimalField(decimal_places=6, default=0.0, max_digits=8)),
                ('is_pos', models.BooleanField(default=False)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='metrics', to='driver.Driver')),
            ],
        ),
    ]