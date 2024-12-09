# Generated by Django 4.2.3 on 2023-10-16 14:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pdai', '0002_alter_predict_results'),
    ]

    operations = [
        migrations.CreateModel(
            name='RF_model',
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
                ('RF_predicted', models.CharField(max_length=20, null=True)),
                ('date_Time', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
