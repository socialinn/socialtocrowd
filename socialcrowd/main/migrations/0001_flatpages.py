# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.core.management import call_command


def add_flatpages_data(apps, schema_editor):
    call_command('loaddata', 'flatpages.json')

def remove_flatpages_data(apps, schema_editor):
    m = apps.get_model('flatpages', 'FlatPage')
    m.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(add_flatpages_data,
                             reverse_code=remove_flatpages_data),
    ]
