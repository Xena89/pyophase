# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 19:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ophasebase', '0004_auto_20170209_2025'),
        ('exam', '0002_auto_20150916_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='group_category',
        ),
        migrations.AddField(
            model_name='assignment',
            name='group_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ophasebase.OphaseCategory',
                                    verbose_name='Gruppenkategorie', null=True, blank=False),
        ),
    ]
