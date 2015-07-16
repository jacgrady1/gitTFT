# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_TFT', '0002_auto_20150715_0631'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('picture', models.ImageField(upload_to=b'photos/teacher_photos')),
                ('course', models.ManyToManyField(to='app_TFT.Course')),
            ],
        ),
    ]
