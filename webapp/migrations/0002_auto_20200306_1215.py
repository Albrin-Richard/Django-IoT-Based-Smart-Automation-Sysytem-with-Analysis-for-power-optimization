# Generated by Django 3.0.3 on 2020-03-06 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devices',
            name='device_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='devices',
            name='device_type',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='room_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
