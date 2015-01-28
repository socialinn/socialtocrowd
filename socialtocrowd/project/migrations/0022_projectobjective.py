# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0021_auto_20141229_1943'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectObjective',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('manifest', models.CharField(max_length=255)),
                ('project', models.ForeignKey(related_name=b'objectives', to='project.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
