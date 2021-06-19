# Generated by Django 2.2.3 on 2020-10-15 09:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0036_posnotification_posreversal_posterminal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ussdvehicleassignment',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='virtualaccount',
            name='driver',
        ),
        migrations.AddField(
            model_name='ussdvehicleassignment',
            name='effective_end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ussdvehicleassignment',
            name='effective_start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='virtualaccount',
            name='effective_end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='virtualaccount',
            name='effective_start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='virtualaccount',
            name='vehicle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_virtual_account', to='driver.Vehicle'),
        ),
    ]