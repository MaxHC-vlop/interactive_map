# Generated by Django 3.1.2 on 2023-01-08 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_auto_20230108_1200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='lat',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='lng',
            new_name='longitude',
        ),
    ]
