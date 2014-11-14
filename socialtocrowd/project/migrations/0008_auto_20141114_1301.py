# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_auto_20141111_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direction',
            name='phone',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
