# Generated by Django 2.2.1 on 2019-06-27 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0018_remove_vehicleexit_tdiff'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='mname',
            field=models.CharField(default='', max_length=20),
        ),
    ]
