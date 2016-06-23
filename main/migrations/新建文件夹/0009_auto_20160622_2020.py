# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20160622_1955'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdataFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='passage',
            name='thefile',
        ),
    ]
