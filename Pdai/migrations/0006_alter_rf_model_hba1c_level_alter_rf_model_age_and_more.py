# Generated by Django 4.2.3 on 2023-11-20 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pdai', '0005_alter_rf_model_hba1c_level_alter_rf_model_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rf_model',
            name='HbA1c_level',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rf_model',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rf_model',
            name='blood_glucose_level',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rf_model',
            name='bmi',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rf_model',
            name='hypertension',
            field=models.IntegerField(),
        ),
    ]
