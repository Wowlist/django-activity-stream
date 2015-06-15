# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

"""
Note the need to run raw sql here.

Error from using built-in migration.

django.db.utils.ProgrammingError: column "action_object_object_id" cannot be cast automatically to type integer
HINT:  Specify a USING expression to perform the conversion.
"""


class Migration(migrations.Migration):

    dependencies = [
        ('actstream', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL("""
        DROP INDEX actstream_action_action_object_object_id;
        DROP INDEX actstream_action_action_object_object_id_like;
        ALTER TABLE actstream_action ALTER COLUMN action_object_object_id TYPE integer USING (trim(action_object_object_id)::integer);

        DROP INDEX actstream_action_actor_object_id;
        DROP INDEX actstream_action_actor_object_id_like;
        ALTER TABLE actstream_action ALTER COLUMN actor_object_id TYPE integer USING (trim(actor_object_id)::integer);

        DROP INDEX actstream_action_target_object_id;
        DROP INDEX actstream_action_target_object_id_like;
        ALTER TABLE actstream_action ALTER COLUMN target_object_id TYPE integer USING (trim(target_object_id)::integer);
        """),
        #migrations.AlterField(
        #    model_name='action',
        #    name='action_object_object_id',
        #    field=models.PositiveIntegerField(null=True, blank=True),
        #    preserve_default=True,
        #),
        #migrations.AlterField(
        #    model_name='action',
        #    name='actor_object_id',
        #    field=models.PositiveIntegerField(),
        #    preserve_default=True,
        #),
        #migrations.AlterField(
        #    model_name='action',
        #    name='target_object_id',
        #    field=models.PositiveIntegerField(null=True, blank=True),
        #    preserve_default=True,
        #),
    ]
