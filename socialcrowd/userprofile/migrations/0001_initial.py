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
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avatar', models.ImageField(upload_to=b'/home/danigm/Projects/work/socialCrowd/socialcrowd/static/media/photos', null=True, verbose_name='Avatar', blank=True)),
                ('web', models.URLField(default=b'', null=True, verbose_name='Web', blank=True)),
                ('twitter', models.CharField(default=b'', max_length=100, null=True, verbose_name=b'Twitter', blank=True)),
                ('facebook', models.CharField(default=b'', max_length=100, null=True, verbose_name=b'Facebook', blank=True)),
                ('user', models.OneToOneField(related_name=b'profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
