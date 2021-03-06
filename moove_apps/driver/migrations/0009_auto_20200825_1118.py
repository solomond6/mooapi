# Generated by Django 2.2.3 on 2020-08-25 11:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0008_auto_20200818_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='plan',
        ),
        migrations.CreateModel(
            name='DriverPlanAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effective_start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('effective_end_date', models.DateTimeField(blank=True, null=True)),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plans', to='driver.Driver')),
                ('plan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plans', to='driver.Plan')),
            ],
        ),
    ]
