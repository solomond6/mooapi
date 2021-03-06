# Generated by Django 2.2.3 on 2020-12-02 13:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0054_auto_20201124_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='active_status',
        ),
        migrations.CreateModel(
            name='DriverStatusAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Inactive', 'Inactive'), ('Active', 'Active'), ('Sick/Leave', 'Sick/Leave'), ('Resigned', 'Resigned')], default='Inactive', max_length=100)),
                ('effective_start_date', models.DateField(default=django.utils.timezone.now)),
                ('effective_end_date', models.DateField(blank=True, null=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver_status', to='driver.Driver')),
            ],
        ),
    ]
