# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-06 01:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('desk', '0002_auto_20170506_0011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='course_name',
            new_name='course_id',
        ),
    ]
