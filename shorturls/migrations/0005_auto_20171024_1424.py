# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-24 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorturls', '0004_auto_20170904_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='shortened_slug',
            field=models.CharField(blank=True, max_length=25, unique=True),
        ),
    ]
