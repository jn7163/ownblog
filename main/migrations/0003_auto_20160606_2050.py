# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160606_2049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accessamount',
            old_name='page',
            new_name='passage',
        ),
    ]
