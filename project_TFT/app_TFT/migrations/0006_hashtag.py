# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('app_TFT', '0005_auto_20150717_0708'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('url', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('course', models.ForeignKey(to='app_TFT.Course')),
            ],
        ),
    ]
