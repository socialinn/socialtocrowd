# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20141102_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='sendtype',
            field=models.CharField(default=b'free', max_length=10, choices=[(b'donorpay', b'donor pay'), (b'ongpay', b'ong pay'), (b'free', b'free')]),
            preserve_default=True,
        ),
    ]
