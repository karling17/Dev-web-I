# Generated by Django 4.2.5 on 2023-11-29 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_rename_tillage_humidity_tillageid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='humidity',
            old_name='tillageId',
            new_name='tillage',
        ),
    ]
