# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('recipe_title', models.CharField(max_length=200)),
                ('recipe_text', models.TextField()),
                ('recipe_date', models.DateField()),
                ('recipe_likes', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'recipe',
            },
            bases=(models.Model,),
        ),
    ]
