# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('feedback', models.TextField()),
                ('rating', models.IntegerField(default=0, null=True)),
                ('dateTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
