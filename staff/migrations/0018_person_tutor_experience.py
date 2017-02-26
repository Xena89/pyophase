# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0017_auto_20170209_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='tutor_experience',
            field=models.PositiveSmallIntegerField(blank=True, default=0, help_text='Wie oft warst du bereits Ophasentutor', verbose_name='Anzahl Tutorentätigkeiten'),
        ),
    ]