# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-16 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20200116_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='website',
            field=models.URLField(default='', null=True),
        ),
    ]
