# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0018_auto_20141217_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping',
            name='status',
            field=models.CharField(default=b'creating', max_length=10, choices=[(b'sent', b'sent'), (b'received', b'received'), (b'confirmed', b'confirmed'), (b'creating', b'creating')]),
        ),
    ]
