# Generated by Django 5.0.6 on 2024-06-18 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_1', '0002_alter_register_data_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register_data',
            old_name='userfristname',
            new_name='userfirstname',
        ),
    ]
