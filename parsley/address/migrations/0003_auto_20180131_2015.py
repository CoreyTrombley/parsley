# Generated by Django 2.0.1 on 2018-01-31 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_auto_20180131_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='line_2',
            field=models.CharField(blank=True, default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='address',
            name='line_1',
            field=models.CharField(max_length=254),
        ),
    ]
