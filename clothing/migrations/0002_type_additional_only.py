# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-20 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='additional_only',
            field=models.BooleanField(default=False, verbose_name='Nur als zusätzliches Kleidungsstück möglich'),
        ),
    ]