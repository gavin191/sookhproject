# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-16 12:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appwithmodels', '0004_auto_20160814_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='furniture',
            name='categories',
            field=models.CharField(default='furniture', max_length=250),
        ),
        migrations.AddField(
            model_name='furniture',
            name='subcategories',
            field=models.CharField(default='furniture', max_length=250),
        ),
    ]