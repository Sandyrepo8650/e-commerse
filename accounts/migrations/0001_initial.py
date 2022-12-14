# Generated by Django 3.2 on 2022-12-13 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=70, unique=True, verbose_name='Email Address')),
                ('phone_number', models.CharField(max_length=15)),
                ('is_active', models.BooleanField(default=True)),
                ('admin', models.BooleanField(default=False)),
                ('superadmin', models.BooleanField(default=False)),
                ('joined_date', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
