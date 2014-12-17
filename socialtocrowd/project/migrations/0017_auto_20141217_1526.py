# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0016_organization_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipping',
            name='show',
        ),
        migrations.AddField(
            model_name='donation',
            name='show',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shipping',
            name='status',
            field=models.CharField(default=b'sent', max_length=10, choices=[(b'sent', b'sent'), (b'received', b'received'), (b'confirmed', b'confirmed'), (b'creating', b'creating')]),
        ),
    ]
