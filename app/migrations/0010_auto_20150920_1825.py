# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20150918_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='descricao',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
