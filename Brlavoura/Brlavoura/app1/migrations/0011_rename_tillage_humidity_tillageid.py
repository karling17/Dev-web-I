# Generated by Django 4.2.5 on 2023-11-29 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_rename_tillageid_humidity_tillage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='humidity',
            old_name='tillage',
            new_name='tillageId',
        ),
    ]