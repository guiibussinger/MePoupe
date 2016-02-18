# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_mes_total_gasto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='descricao',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='validada',
            field=models.BooleanField(verbose_name='Validar agora', default=False),
        ),
        migrations.AlterUniqueTogether(
            name='categoria',
            unique_together=set([('id', 'descricao')]),
        ),
    ]
