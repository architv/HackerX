# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0002_user_github_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='required_github_data',
            field=jsonfield.fields.JSONField(default='sdsadas'),
            preserve_default=False,
        ),
    ]
