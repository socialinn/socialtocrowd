# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0012_donation_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collaborator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.ImageField(upload_to=b'collaborators')),
                ('link', models.CharField(max_length=255)),
                ('project', models.ForeignKey(related_name=b'collaborators', to='project.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
