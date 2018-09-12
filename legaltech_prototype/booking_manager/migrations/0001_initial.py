# Generated by Django 2.0.6 on 2018-09-11 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('lawyer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default='Monday', max_length=15)),
                ('start_time', models.TimeField(default=0)),
                ('end_time', models.TimeField(default=0)),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Booked', 'Booked')], default='Available', max_length=15)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='booking_manager.Location')),
            ],
        ),
    ]