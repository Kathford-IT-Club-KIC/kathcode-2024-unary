# Generated by Django 4.2.5 on 2024-06-28 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(max_length=100)),
                ('restaurant_address', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
