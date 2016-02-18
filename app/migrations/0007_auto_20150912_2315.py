# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_despesa_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaMes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('objetivo', models.FloatField(null=True, default=None, blank=True)),
                ('gasto', models.FloatField(default=0.0)),
            ],
        ),
        migrations.AlterField(
            model_name='categoria',
            name='descricao',
            field=models.CharField(null=True, max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='categoriames',
            name='categoria',
            field=models.ForeignKey(to='app.Categoria'),
        ),
        migrations.AddField(
            model_name='categoriames',
            name='mes',
            field=models.ForeignKey(to='app.Mes'),
        ),
        migrations.AlterUniqueTogether(
            name='categoriames',
            unique_together=set([('categoria', 'mes')]),
        ),
    ]
