# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20160622_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updatafile',
            name='url',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
