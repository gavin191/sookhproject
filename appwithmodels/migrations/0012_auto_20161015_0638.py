# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-15 06:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('appwithmodels', '0011_auto_20161015_0638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessories_sub_category',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 15, 6, 38, 52, 209747, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mobiles_sub_category',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 15, 6, 38, 52, 209747, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tablets_sub_category',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 15, 6, 38, 52, 209747, tzinfo=utc)),
        ),
    ]
