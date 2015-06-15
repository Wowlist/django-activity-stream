# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actstream', '0002_auto_20150615_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='action_object_object_id',
            field=models.PositiveIntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='action',
            name='actor_object_id',
            field=models.PositiveIntegerField(db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='action',
            name='target_object_id',
            field=models.PositiveIntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
    ]
