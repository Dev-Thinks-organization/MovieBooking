# Generated by Django 3.2.9 on 2021-11-27 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0008_alter_bookings_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='show',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
        migrations.RemoveField(
            model_name='seat',
            name='booking',
        ),
        migrations.DeleteModel(
            name='BookedSeat',
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
