# Generated by Django 3.2.9 on 2021-11-27 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_alter_seat_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='promocode',
            name='usedTimes',
            field=models.IntegerField(default=0),
        ),
    ]
