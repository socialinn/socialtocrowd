# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(blank=True)),
                ('show', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(related_name=b'shipping', to='project.Project')),
                ('user', models.ForeignKey(related_name=b'shipping', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='donation',
            name='created',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='donor',
        ),
        migrations.AddField(
            model_name='donation',
            name='delivery',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='donation',
            name='shipping',
            field=models.ForeignKey(related_name=b'donations', default=1, to='project.Shipping'),
            preserve_default=False,
        ),
    ]
