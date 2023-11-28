# Generated by Django 4.2.5 on 2023-11-28 23:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_rename_farmid_harvest_farm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pictures',
            name='file',
        ),
        migrations.AddField(
            model_name='pictures',
            name='filelink',
            field=models.CharField(default=django.utils.timezone.now, max_length=400),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='humidity',
            name='humidity',
            field=models.FloatField(),
        ),
    ]
