# Generated by Django 2.2.3 on 2020-12-04 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0057_auto_20201203_1240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uberreconciliaition',
            old_name='All_Drivers_date',
            new_name='all_drivers_date',
        ),
    ]