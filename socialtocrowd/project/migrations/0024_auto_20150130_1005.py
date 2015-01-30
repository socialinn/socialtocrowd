# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0023_project_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cooperation',
            name='when',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cooperation',
            name='where',
            field=models.ForeignKey(related_name=b'cooperations', blank=True, to='project.Direction', null=True),
        ),
    ]
