# Generated by Django 2.2.3 on 2020-08-31 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0013_driverbankaccount_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drivervehicleassignment',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='driver_assingment', to='driver.Driver'),
        ),
        migrations.AlterField(
            model_name='drivervehicleassignment',
            name='vehicle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_assingment', to='driver.Vehicle'),
        ),
    ]
