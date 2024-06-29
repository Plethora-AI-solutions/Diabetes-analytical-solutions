# Generated by Django 4.2.3 on 2023-11-20 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pdai', '0004_rf_model_rf_prob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rf_model',
            name='HbA1c_level',
            field=models.IntegerField(max_length=35),
        ),
        migrations.AlterField(
            model_name='rf_model',
            name='age',
            field=models.IntegerField(max_length=30),
        ),
        migrations.AlterField(
            model_name='rf_model',
            name='blood_glucose_level',
            field=models.IntegerField(max_length=25),
        ),
        migrations.AlterField(
            model_name='rf_model',
            name='bmi',
            field=models.IntegerField(max_length=55),
        ),
        migrations.AlterField(
            model_name='rf_model',
            name='hypertension',
            field=models.IntegerField(max_length=30),
        ),
    ]