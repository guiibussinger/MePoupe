# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20150912_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='despesa',
            name='categoria',
            field=models.ForeignKey(null=True, blank=True, to='app.Categoria'),
        ),
    ]
