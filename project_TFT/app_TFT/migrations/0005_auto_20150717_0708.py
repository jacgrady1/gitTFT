# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_TFT', '0004_auto_20150716_0711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('num', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='alias',
            field=models.CharField(default=datetime.datetime(2015, 7, 17, 7, 8, 24, 922606, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lecture',
            name='course',
            field=models.ForeignKey(to='app_TFT.Course'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='lecture',
            field=models.ForeignKey(to='app_TFT.Lecture'),
        ),
    ]
