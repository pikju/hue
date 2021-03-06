# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-02-03 16:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

from desktop.conf import ENABLE_CONNECTORS


# Currently would need to be reran if enabling connector only post the first rebase of this commit


class Migration(migrations.Migration):

    dependencies = [
        ('desktop', '0010_auto_20200115_0908'),
        ('useradmin', '0002_userprofile_json_data'),
    ]

    if ENABLE_CONNECTORS.get():
      operations = [
          migrations.AlterModelOptions(
              name='huepermission',
              options={'verbose_name': 'Connector permission', 'verbose_name_plural': 'Connector permissions'},
          ),
          migrations.AddField(
              model_name='huepermission',
              name='connector',
              field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='desktop.Connector'),
              preserve_default=False,
          ),
          migrations.AlterUniqueTogether(
              name='huepermission',
              unique_together=set([('connector', 'action')]),
          ),
      ]
    else:
      operations = []
