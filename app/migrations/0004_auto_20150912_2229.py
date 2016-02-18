# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_mes_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metausuario',
            name='userid',
            field=models.OneToOneField(serialize=False, primary_key=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
