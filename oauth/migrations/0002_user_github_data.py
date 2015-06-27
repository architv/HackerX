# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='github_data',
            field=jsonfield.fields.JSONField(default='fdsdds'),
            preserve_default=False,
        ),
    ]
