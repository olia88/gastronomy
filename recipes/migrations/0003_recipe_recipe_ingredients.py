# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_ingredients',
            field=models.TextField(default=19.4),
            preserve_default=False,
        ),
    ]
