# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20160606_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='passage',
            name='changetime',
            field=models.DateTimeField(null=True, verbose_name=django.utils.timezone.now, blank=True),
        ),
    ]
