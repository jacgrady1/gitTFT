# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_TFT', '0003_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='picture',
            field=models.ImageField(upload_to=b'photos/teacher_photos', blank=True),
        ),
    ]
