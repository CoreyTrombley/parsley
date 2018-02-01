# Generated by Django 2.0.1 on 2018-01-31 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='patient',
        ),
        migrations.AlterField(
            model_name='phone',
            name='number',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='phone',
            name='type',
            field=models.CharField(blank=True, default='mobile', max_length=20),
        ),
    ]