# Generated by Django 2.2.3 on 2020-12-03 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0056_uberreconciliaition'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OpsMetric',
        ),
        migrations.DeleteModel(
            name='OpsMetricSummary',
        ),
    ]
