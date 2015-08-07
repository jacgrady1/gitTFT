# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_TFT', '0010_auto_20150806_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='role',
            field=models.CharField(default=b'Lecturer', max_length=10, choices=[(b'Lecturer', b'Lecturer'), (b'Coach', b'Coach')]),
        ),
    ]
