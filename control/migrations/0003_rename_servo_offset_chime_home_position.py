# Generated by Django 3.2.3 on 2021-12-14 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0002_auto_20211213_0056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chime',
            old_name='servo_offset',
            new_name='home_position',
        ),
    ]
