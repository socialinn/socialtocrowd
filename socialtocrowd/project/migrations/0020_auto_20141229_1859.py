# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0019_auto_20141218_0024'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cooperation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('what', models.TextField()),
                ('when', models.DateTimeField()),
                ('quantity', models.IntegerField(default=1)),
                ('project', models.ForeignKey(related_name=b'cooperations', to='project.Project')),
                ('where', models.ForeignKey(related_name=b'cooperations', to='project.Direction')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='donation',
            name='cooperation',
            field=models.ForeignKey(related_name=b'cooperations', to='project.Cooperation', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='donation',
            name='type_donation',
            field=models.CharField(default=b'T', max_length=1, choices=[(b'C', b'Cooperation'), (b'T', b'Thing')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='donation',
            name='thing',
            field=models.ForeignKey(related_name=b'donations', to='project.Thing', null=True),
        ),
    ]
