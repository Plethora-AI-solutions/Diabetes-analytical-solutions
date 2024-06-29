# Generated by Django 4.2.3 on 2023-10-14 20:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='predict',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=40)),
                ('sname', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=90)),
                ('HbA1c_level', models.IntegerField()),
                ('blood_glucose_level', models.IntegerField()),
                ('age', models.IntegerField()),
                ('bmi', models.IntegerField()),
                ('hypertension', models.IntegerField()),
                ('date_Time', models.DateTimeField(default=datetime.datetime.now)),
                ('results', models.IntegerField()),
            ],
        ),
    ]