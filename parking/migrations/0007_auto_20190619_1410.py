# Generated by Django 2.2.1 on 2019-06-19 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0006_vehicleentry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicleentry',
            name='intime',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
