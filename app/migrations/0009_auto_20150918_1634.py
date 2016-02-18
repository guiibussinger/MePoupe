# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_mes_total_gasto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='validada',
            field=models.BooleanField(default=False, verbose_name='Validar agora'),
        ),
    ]
