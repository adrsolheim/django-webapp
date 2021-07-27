# Generated by Django 3.2.5 on 2021-07-25 16:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('style', models.CharField(max_length=30)),
                ('volume', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('start_date', models.DateField(auto_now_add=True, verbose_name='brewed')),
                ('end_date', models.DateField(blank=True, verbose_name='finished')),
                ('score', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('comment', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'ordering': ['-start_date'],
            },
        ),
    ]