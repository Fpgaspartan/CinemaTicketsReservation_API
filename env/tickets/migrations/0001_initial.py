# Generated by Django 5.1.4 on 2024-12-07 19:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall', models.CharField(max_length=10)),
                ('movie', models.CharField(max_length=10)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat', models.CharField(max_length=5)),
                ('status', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('price', models.FloatField()),
                ('discount', models.FloatField()),
                ('total', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cancelled_at', models.DateTimeField(null=True)),
                ('cancelled_reason', models.CharField(max_length=255, null=True)),
                ('cancelled_by', models.CharField(max_length=30, null=True)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.guest')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.movie')),
            ],
        ),
    ]
