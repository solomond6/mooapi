# Generated by Django 2.2.3 on 2020-11-03 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0050_opsmetricsummary_total_return'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opsmetric',
            name='lasdri_attendance',
        ),
        migrations.RemoveField(
            model_name='opsmetric',
            name='lasdri_card',
        ),
        migrations.RemoveField(
            model_name='opsmetric',
            name='lasdri_form',
        ),
        migrations.RemoveField(
            model_name='opsmetric',
            name='lassra_attendance',
        ),
        migrations.RemoveField(
            model_name='opsmetric',
            name='lassra_card',
        ),
    ]
