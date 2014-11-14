# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0005_auto_20141110_0329'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='status',
            field=models.CharField(default=b'pending', max_length=10, choices=[(b'pending', b'pending'), (b'active', b'active'), (b'deleted', b'deleted')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organization',
            name='user',
            field=models.ForeignKey(related_name=b'organizations', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
