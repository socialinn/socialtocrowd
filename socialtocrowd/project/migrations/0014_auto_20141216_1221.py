# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0013_collaborator'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='facebook',
            field=models.CharField(default=b'https://www.facebook.com/', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='googleplus',
            field=models.CharField(default=b'https://plus.google.com/', max_length=255, verbose_name=b'Google+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='twitter',
            field=models.CharField(default=b'https://twitter.com/', max_length=150),
            preserve_default=True,
        ),
    ]
