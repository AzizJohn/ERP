# Generated by Django 4.2 on 2023-04-14 10:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personnel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('work_start_time', models.DateTimeField(default=datetime.time(10, 0))),
                ('arrival_time', models.DateTimeField()),
                ('personnel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='personnel.personnel')),
            ],
            options={
                'verbose_name': 'Attendance',
                'verbose_name_plural': 'Attendances',
            },
        ),
    ]
