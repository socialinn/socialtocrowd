# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0017_auto_20141217_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='show',
            field=models.BooleanField(default=True),
        ),
    ]
