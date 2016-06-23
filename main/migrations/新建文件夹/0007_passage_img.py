# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_passage_changetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='passage',
            name='img',
            field=models.FileField(default=b'', upload_to=b'media/', blank=True),
        ),
    ]
