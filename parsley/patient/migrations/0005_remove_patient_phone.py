# Generated by Django 2.0.1 on 2018-01-31 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_patient_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='phone',
        ),
    ]
