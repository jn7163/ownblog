# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_passage_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passage',
            old_name='img',
            new_name='thefile',
        ),
    ]
