# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-19 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0023_auto_20170804_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorgroup',
            name='picture',
            field=models.FileField(blank=True, upload_to='grouppicture/'),
        ),
    ]
