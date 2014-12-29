# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0020_auto_20141229_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='cooperation',
            field=models.ForeignKey(related_name=b'cooperations', blank=True, to='project.Cooperation', null=True),
        ),
        migrations.AlterField(
            model_name='donation',
            name='thing',
            field=models.ForeignKey(related_name=b'donations', blank=True, to='project.Thing', null=True),
        ),
    ]
