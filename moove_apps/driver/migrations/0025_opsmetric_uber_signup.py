# Generated by Django 2.2.3 on 2020-09-08 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0024_auto_20200907_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='opsmetric',
            name='uber_signup',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
