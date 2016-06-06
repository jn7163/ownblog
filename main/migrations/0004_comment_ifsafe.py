# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20160606_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='ifsafe',
            field=models.BooleanField(default=False),
        ),
    ]
