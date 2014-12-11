# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_auto_20141211_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='img',
            field=models.ImageField(null=True, upload_to=b'donations', blank=True),
            preserve_default=True,
        ),
    ]
