# Generated by Django 3.1.1 on 2020-12-10 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0059_driverscorecard'),
    ]

    operations = [
        migrations.AddField(
            model_name='uberreconciliaition',
            name='master_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
