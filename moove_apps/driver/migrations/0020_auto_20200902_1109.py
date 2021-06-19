# Generated by Django 2.2.3 on 2020-09-02 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0019_auto_20200902_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drivergpa',
            name='current_gpa',
            field=models.DecimalField(decimal_places=8, default=5, max_digits=50),
        ),
        migrations.AlterField(
            model_name='drivergpa',
            name='total_deduction',
            field=models.DecimalField(decimal_places=8, default=0, max_digits=50),
        ),
    ]