# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_TFT', '0008_auto_20150730_0448'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='school',
            field=models.CharField(default=datetime.datetime(2015, 7, 30, 5, 14, 57, 11117, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
