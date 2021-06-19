# Generated by Django 3.1.1 on 2020-12-07 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0058_auto_20201204_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='DriverScoreCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conctact_type', models.CharField(choices=[('offline_driver', 'Offline Driver(Outbound)'), ('kpi_check', 'KPIs Check(Outbound)'), ('inbound', 'Inbound')], max_length=100)),
                ('team_captain', models.CharField(blank=True, max_length=100, null=True)),
                ('last_seen', models.DateTimeField(blank=True, null=True)),
                ('reason_offline', models.JSONField(default=list)),
                ('immediate_attention', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True)),
                ('kpi_not_met', models.JSONField(default=list)),
                ('reason_target_not_met', models.JSONField(default=list)),
                ('comment', models.TextField(blank=True, null=True)),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='driver_score_card', to='driver.driver')),
            ],
        ),
    ]