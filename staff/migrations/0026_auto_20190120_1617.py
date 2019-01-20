# Generated by Django 2.0.10 on 2019-01-20 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0025_auto_20171005_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='helperjob',
            name='minimum_number_required',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Minimal benötigte Anzahl an Helfern'),
        ),
        migrations.AddField(
            model_name='helperjob',
            name='optimal_number_needed',
            field=models.PositiveSmallIntegerField(default=2, verbose_name='Optimal benötigte Anzahl an Helfern'),
        ),
    ]
