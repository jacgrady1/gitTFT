# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_TFT', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='start_time',
            field=models.TimeField(null=True),
        ),
    ]
