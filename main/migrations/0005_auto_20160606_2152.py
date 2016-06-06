# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_comment_ifsafe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='ifshowip',
        ),
        migrations.AddField(
            model_name='comment',
            name='ifhideip',
            field=models.BooleanField(default=True),
        ),
    ]
