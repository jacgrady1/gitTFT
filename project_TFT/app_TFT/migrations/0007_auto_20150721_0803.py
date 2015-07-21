# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_TFT', '0006_hashtag'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='group_price',
            field=models.FloatField(default=0, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='promotion_info',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
