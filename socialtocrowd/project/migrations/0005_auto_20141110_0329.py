# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_shippingcompany'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=255)),
                ('pos', django.contrib.gis.db.models.fields.PointField(help_text=b'Represented as (longitude, latitude)', srid=4326, null=True, blank=True)),
                ('timetable', models.CharField(max_length=255)),
                ('phone', models.IntegerField(null=True, blank=True)),
                ('project', models.ForeignKey(related_name=b'directions', to='project.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='project',
            name='shipping_address',
        ),
        migrations.AddField(
            model_name='donation',
            name='direction',
            field=models.ForeignKey(related_name=b'donations', default=1, to='project.Direction'),
            preserve_default=False,
        ),
    ]
