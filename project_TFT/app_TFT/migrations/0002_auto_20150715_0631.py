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
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=300)),
                ('answer', models.CharField(max_length=2000, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='brief',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2015, 7, 15, 6, 31, 25, 650979, tzinfo=utc), blank=True),
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
        migrations.AddField(
            model_name='question',
            name='course',
            field=models.ForeignKey(to='app_TFT.Course'),
        ),
    ]
