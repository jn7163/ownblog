# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessamount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ifshowip', models.BooleanField()),
                ('ip', models.CharField(max_length=20)),
                ('body', models.TextField()),
                ('time', models.DateTimeField(verbose_name=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Passage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('time', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('info', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='passage',
            field=models.ForeignKey(to='main.Passage'),
        ),
        migrations.AddField(
            model_name='accessamount',
            name='page',
            field=models.ForeignKey(to='main.Passage'),
        ),
    ]
