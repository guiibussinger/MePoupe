# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100, null=True)),
                ('usuario', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('descricao', models.CharField(blank=True, max_length=100, null=True, default='Sem descricao')),
                ('usuario', models.IntegerField(default=0)),
                ('valor', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('dataCriacao', models.DateField(default=datetime.date.today)),
                ('dataValidacao', models.DateField(null=True, verbose_name='Validar em (opcional):', blank=True)),
                ('validada', models.BooleanField(verbose_name='Auto-Validar', default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Mes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('ano', models.IntegerField()),
                ('balanco', models.FloatField(default=0.0)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MetaUsuario',
            fields=[
                ('userid', models.IntegerField(primary_key=True, serialize=False)),
                ('dataCriacao', models.DateField(auto_now_add=True, verbose_name='Data de Criacao')),
            ],
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('descricao', models.CharField(blank=True, max_length=100, null=True, default='Sem descricao')),
                ('usuario', models.IntegerField()),
                ('valor', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('dataCriacao', models.DateField(default=datetime.date.today)),
                ('dataValidacao', models.DateField(null=True, verbose_name='Validar em (opcional):', blank=True)),
                ('validada', models.BooleanField(verbose_name='Auto-Validar', default=False)),
                ('mes', models.ForeignKey(null=True, to='app.Mes')),
            ],
        ),
        migrations.AddField(
            model_name='despesa',
            name='mes',
            field=models.ForeignKey(null=True, to='app.Mes'),
        ),
    ]
