# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_TFT', '0007_auto_20150721_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='role',
            field=models.CharField(default=b'l', max_length=1, choices=[(b'l', b'Lecturer'), (b'c', b'Coach')]),
        ),
    ]
