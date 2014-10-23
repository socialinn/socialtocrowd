# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('info', models.TextField(blank=True)),
                ('status', models.CharField(default=b'sent', max_length=10, choices=[(b'sent', b'sent'), (b'received', b'received'), (b'confirmed', b'confirmed')])),
                ('quantity', models.IntegerField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('donor', models.ForeignKey(related_name=b'donations', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('img', models.ImageField(null=True, upload_to=b'ongs', blank=True)),
                ('city', models.CharField(max_length=255)),
                ('province', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('img', models.ImageField(null=True, upload_to=b'projects', blank=True)),
                ('shipping_address', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ong', models.ForeignKey(related_name=b'projects', to='project.Organization')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
                ('quantity', models.IntegerField(default=1)),
                ('project', models.ForeignKey(related_name=b'things', to='project.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='donation',
            name='thing',
            field=models.ForeignKey(related_name=b'donations', to='project.Thing'),
            preserve_default=True,
        ),
    ]
