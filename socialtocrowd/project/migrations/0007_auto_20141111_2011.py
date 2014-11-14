# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_auto_20141110_1902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='delivery',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='direction',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='sendtype',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='status',
        ),
        migrations.AddField(
            model_name='shipping',
            name='delivery',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shipping',
            name='direction',
            field=models.ForeignKey(related_name=b'shipping', to='project.Direction', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shipping',
            name='status',
            field=models.CharField(default=b'sent', max_length=10, choices=[(b'sent', b'sent'), (b'received', b'received'), (b'confirmed', b'confirmed')]),
            preserve_default=True,
        ),
    ]
