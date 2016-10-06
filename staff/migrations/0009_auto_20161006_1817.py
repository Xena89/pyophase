# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 16:17
from __future__ import unicode_literals

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0008_auto_20160822_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Deine Handynummer brauchen wir um dich schnell erreichen zu können.', max_length=128, verbose_name='Handynummer'),
        ),
    ]
