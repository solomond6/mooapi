# Generated by Django 2.2.3 on 2020-11-02 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0047_auto_20201102_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='opsmetric',
            name='vehicle_first_trip',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]