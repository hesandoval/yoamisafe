# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yoamisafe', '0002_auto_20141101_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='latitude',
            field=models.DecimalField(max_digits=20, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='incident',
            name='longitude',
            field=models.DecimalField(max_digits=20, decimal_places=3),
        ),
    ]
