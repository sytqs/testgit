# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MsgPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-datetime'],
            },
        ),
    ]
