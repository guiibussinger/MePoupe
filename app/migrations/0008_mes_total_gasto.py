# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20150912_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='mes',
            name='total_gasto',
            field=models.FloatField(default=0.0),
        ),
    ]
