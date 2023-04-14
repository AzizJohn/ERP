# Generated by Django 4.2 on 2023-04-14 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personnel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('start_date', models.DateField(verbose_name='Start date')),
                ('finish_date', models.DateField(verbose_name='Finish date')),
                ('num_of_trainee', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=300)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personnel.personnel')),
            ],
            options={
                'verbose_name': 'Internship',
                'verbose_name_plural': 'Internships',
            },
        ),
    ]
