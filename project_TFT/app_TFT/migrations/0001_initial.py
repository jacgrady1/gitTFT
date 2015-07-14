# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('picture', models.ImageField(upload_to=b'photos/course_photos')),
                ('start_date', models.DateField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
