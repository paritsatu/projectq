# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-16 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artikel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=255)),
                ('isi', models.TextField()),
                ('kategori', models.CharField(max_length=255)),
                ('dibuat', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_published', models.NullBooleanField(default=False)),
                ('published', models.DateTimeField(null=True)),
                ('slug', models.SlugField(blank=True, editable=False)),
            ],
            options={
                'permissions': (('publish_artikel', 'Can publish artikel'),),
                'default_permissions': ('add', 'change', 'delete'),
            },
        ),
    ]
