# Generated by Django 2.2.3 on 2020-08-15 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0004_auto_20200814_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='active_status',
            field=models.CharField(choices=[('Not Active', 'Not Active'), ('Active', 'Active'), ('Sick/Leave', 'Sick/Leave'), ('Resigned', 'Resigned')], default='Not Active', max_length=100),
        ),
        migrations.AddField(
            model_name='driver',
            name='uber_status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Waitlisted', 'Waitlisted')], default='Active', max_length=100),
        ),
        migrations.AlterField(
            model_name='driver',
            name='approval_status',
            field=models.CharField(choices=[('Approved', 'Approved'), ('In Progress', 'In Progress')], default='In Progress', max_length=100),
        ),
        migrations.AlterField(
            model_name='driver',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='uber_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='uber_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='assignment_status',
            field=models.CharField(choices=[('Assigned', 'Assigned'), ('Not Assigned', 'Not Assigned')], max_length=100, null=True),
        ),
    ]
