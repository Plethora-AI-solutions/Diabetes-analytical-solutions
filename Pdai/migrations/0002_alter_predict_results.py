# Generated by Django 4.2.3 on 2023-10-14 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pdai', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predict',
            name='results',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
