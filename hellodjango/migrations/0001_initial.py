# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hello',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
                ('description', models.TextField(max_length=250, null=True, blank=True)),
                ('created_at', models.DateTimeField()),
                ('modified_at', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
