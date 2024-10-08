# Generated by Django 4.2.13 on 2024-07-18 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_booking_rental_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='child_seat_option',
            field=models.CharField(blank=True, choices=[('0-9 kg', 'Baby seat (0-9 kg)'), ('9-18 kg', 'Child seat (9-18 kg)'), ('booster', 'Booster seat (15-36 kg)')], max_length=20, null=True),
        ),
    ]
