# Generated by Django 2.0.1 on 2018-01-31 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0003_auto_20180131_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='zip',
            field=models.CharField(max_length=5),
        ),
    ]
