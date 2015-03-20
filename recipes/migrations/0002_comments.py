# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('comments_text', models.TextField()),
                ('comments_date', models.DateField()),
                ('comments_recipe', models.ForeignKey(to='recipes.Recipe')),
            ],
            options={
                'db_table': 'comments',
            },
            bases=(models.Model,),
        ),
    ]
