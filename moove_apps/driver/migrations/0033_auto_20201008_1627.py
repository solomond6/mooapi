# Generated by Django 2.2.3 on 2020-10-08 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0032_auto_20200916_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='created_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='updated_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
