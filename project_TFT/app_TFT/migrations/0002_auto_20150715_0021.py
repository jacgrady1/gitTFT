# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_TFT', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='brief',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2015, 7, 15, 0, 21, 14, 75919, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='start_date',
            field=models.DateField(blank=True),
        ),
    ]
