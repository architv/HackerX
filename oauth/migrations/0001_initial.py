# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('user_name', models.CharField(unique=True, max_length=20)),
                ('avatar_url', models.URLField()),
                ('num_followers', models.IntegerField()),
                ('num_following', models.IntegerField()),
                ('access_token', models.CharField(max_length=250)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('num_repos_public', models.IntegerField()),
                ('location', models.CharField(max_length=100)),
                ('blog_url', models.URLField()),
                ('company', models.CharField(max_length=75)),
            ],
            options={
                'db_table': 'github_user',
            },
        ),
    ]
