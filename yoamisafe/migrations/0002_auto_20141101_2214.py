# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yoamisafe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='date',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='description',
            field=models.TextField(max_length=100),
        ),
    ]
