# Generated by Django 4.2.3 on 2023-07-30 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('slotBooking', '0003_parking'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservationSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('parking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slotBooking.parking')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
