# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0024_auto_20150130_1005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='objetives',
        ),
    ]
