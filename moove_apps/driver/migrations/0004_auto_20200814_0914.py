# Generated by Django 2.2.3 on 2020-08-14 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0003_auto_20200814_0832'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uberpayment',
            old_name='date_exact',
            new_name='date_extract',
        ),
    ]
