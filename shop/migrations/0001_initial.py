# Generated by Django 4.0.4 on 2022-06-26 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet_food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mark', models.CharField(max_length=30)),
                ('size', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Pet_toys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mark', models.CharField(max_length=30)),
                ('size', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Pet_vet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mark', models.CharField(max_length=30)),
                ('size', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('price', models.FloatField()),
            ],
        ),
    ]
